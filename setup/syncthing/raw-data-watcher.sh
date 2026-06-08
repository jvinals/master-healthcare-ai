#!/usr/bin/env bash
# raw-data-watcher.sh — vigila raw_data/ y dispara la ingestión.
#
# Diseño:
#   * fswatch escucha cambios recursivos en raw_data/.
#   * Cuando llega un evento, se programa la ingestión para correr en
#     ``DEBOUNCE_SECS`` segundos. Si llegan más eventos antes (típico en
#     una sincronización Syncthing con varios ficheros nuevos), se
#     resetea el temporizador — sólo corremos una vez al final.
#   * Antes de ingestar comprobamos que el árbol está "estable": ningún
#     fichero modificado en los últimos STABLE_SECS segundos. Esto evita
#     ingestar un PDF a medio sincronizar.
#   * Logs en setup/syncthing/logs/watcher.log (rotación manual).
#
# Requisitos en el Mac mini:
#   brew install fswatch
#   python3 con las deps de la pipeline (pymupdf, python-docx, etc.)
#
# Variables que puedes sobrescribir antes de invocarlo:
#   REPO_ROOT       — raíz del repo "documentation/" (auto-detectada por defecto).
#   RAW_DIR         — directorio a vigilar (por defecto: <profile>/raw_data).
#   DEBOUNCE_SECS   — espera tras el último evento antes de ingestar (10).
#   STABLE_SECS     — sin modificaciones recientes antes de ingestar (20).
#   PYTHON_BIN      — intérprete a usar (autodetectado).

set -euo pipefail

# ------------------------------------------------------------------ #
# Configuración
# ------------------------------------------------------------------ #

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# documentation/setup/syncthing/  ->  documentation/
REPO_ROOT="${REPO_ROOT:-$(cd "$SCRIPT_DIR/../.." && pwd)}"
# documentation/  ->  perfil
PROFILE_ROOT="$(cd "$REPO_ROOT/.." && pwd)"
RAW_DIR="${RAW_DIR:-$PROFILE_ROOT/raw_data}"
DEBOUNCE_SECS="${DEBOUNCE_SECS:-10}"
STABLE_SECS="${STABLE_SECS:-20}"
PYTHON_BIN="${PYTHON_BIN:-$(command -v python3)}"
LOG_DIR="$SCRIPT_DIR/logs"
LOG_FILE="$LOG_DIR/watcher.log"
LOCK_FILE="$LOG_DIR/.ingest.lock"
PENDING_FILE="$LOG_DIR/.pending"

mkdir -p "$LOG_DIR"

log() {
  printf '%s %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" | tee -a "$LOG_FILE"
}

# ------------------------------------------------------------------ #
# Sanidad
# ------------------------------------------------------------------ #

if ! command -v fswatch >/dev/null 2>&1; then
  log "ERROR: fswatch no encontrado. Instálalo con:  brew install fswatch"
  exit 127
fi

if [[ ! -d "$RAW_DIR" ]]; then
  log "ERROR: RAW_DIR no existe: $RAW_DIR"
  exit 2
fi

if [[ ! -x "$PYTHON_BIN" ]]; then
  log "ERROR: PYTHON_BIN no es ejecutable: $PYTHON_BIN"
  exit 2
fi

log "watcher arrancando"
log "  REPO_ROOT      = $REPO_ROOT"
log "  RAW_DIR        = $RAW_DIR"
log "  DEBOUNCE_SECS  = $DEBOUNCE_SECS"
log "  STABLE_SECS    = $STABLE_SECS"
log "  PYTHON_BIN     = $PYTHON_BIN"

# ------------------------------------------------------------------ #
# Ingestión (lo que se ejecuta cuando los eventos paran de llegar)
# ------------------------------------------------------------------ #

run_ingest() {
  # Lock para no solapar invocaciones.
  if ! mkdir "$LOCK_FILE" 2>/dev/null; then
    log "ingestión ya en curso — se omite esta ronda"
    return 0
  fi
  trap 'rmdir "$LOCK_FILE" 2>/dev/null || true' RETURN

  # Espera de estabilidad: ningún fichero modificado en los últimos
  # STABLE_SECS segundos. Si Syncthing aún está copiando algo grande,
  # esperamos.
  local waits=0
  while :; do
    local newest_age
    newest_age=$(find "$RAW_DIR" -type f -not -name '.*' -newermt "-$STABLE_SECS seconds" 2>/dev/null | head -n1 || true)
    if [[ -z "$newest_age" ]]; then
      break
    fi
    waits=$((waits + 1))
    if (( waits > 30 )); then
      log "WARN: raw_data sigue cambiando tras 30 reintentos; ingiero igualmente"
      break
    fi
    log "  …todavía hay ficheros modificados en <${STABLE_SECS}s, espero"
    sleep "$STABLE_SECS"
  done

  log "→ python scripts/ingest.py"
  if ! "$PYTHON_BIN" "$REPO_ROOT/scripts/ingest.py" >>"$LOG_FILE" 2>&1; then
    log "ERROR: ingest.py falló (continúo de todas formas)"
  fi

  log "→ python scripts/validate_registry.py"
  "$PYTHON_BIN" "$REPO_ROOT/scripts/validate_registry.py" >>"$LOG_FILE" 2>&1 || \
    log "WARN: validate_registry.py marcó errores — revisar log"

  log "→ python scripts/build_dashboard.py"
  "$PYTHON_BIN" "$REPO_ROOT/scripts/build_dashboard.py" >>"$LOG_FILE" 2>&1 || \
    log "WARN: build_dashboard.py falló"

  log "ingestión completada"
}

# ------------------------------------------------------------------ #
# Debouncer: cuando se planifica una ingestión, espera DEBOUNCE_SECS;
# si llegan más eventos en ese intervalo, se posterga.
# ------------------------------------------------------------------ #

schedule_ingest() {
  # Marca "pendiente desde ahora" — el watcher loop se encarga de
  # esperar y ejecutar.
  date +%s > "$PENDING_FILE"
}

debouncer_loop() {
  while :; do
    sleep 2
    [[ -f "$PENDING_FILE" ]] || continue
    local last_event
    last_event=$(<"$PENDING_FILE")
    local now elapsed
    now=$(date +%s)
    elapsed=$((now - last_event))
    if (( elapsed >= DEBOUNCE_SECS )); then
      rm -f "$PENDING_FILE"
      log "debounce satisfecho (${elapsed}s sin eventos) — disparo ingestión"
      run_ingest
    fi
  done
}

# Arranca el debouncer en background
debouncer_loop &
DEBOUNCER_PID=$!
trap 'kill $DEBOUNCER_PID 2>/dev/null || true' EXIT

# ------------------------------------------------------------------ #
# Bucle principal: fswatch hace stream de cambios
# ------------------------------------------------------------------ #

# --exclude '\.tmp$' --exclude '\.DS_Store$' descarta cruft típico.
# --latency 2 agrupa eventos cercanos a nivel de fswatch.
fswatch \
  --latency 2 \
  --recursive \
  --exclude '/\.' \
  --exclude '\.tmp$' \
  --exclude '\.swp$' \
  --exclude '~$' \
  --exclude '\.syncthing\..*\.tmp$' \
  --exclude '\.stfolder' \
  "$RAW_DIR" |
while read -r changed_path; do
  log "evento: $changed_path"
  schedule_ingest
done
