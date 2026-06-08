# Runbook — Syncthing + watcher para `raw_data/`

> **Objetivo:** poder dejar caer documentos (PDF/DOCX/PPTX/XLSX) desde cualquier dispositivo conectado a tu Tailnet en `raw_data/`, y que ~30 s después estén ingeridos, registrados, validados y reflejados en el dashboard.
>
> **Arquitectura:**
>
> ```
> [portátil] ─┐
> [móvil]    ─┼─► Syncthing P2P ─► Mac mini: raw_data/ ─► fswatch ─► watcher.sh
> [otro]     ─┘                                                       │
>                                                                     ├─► ingest.py
>                                                                     ├─► validate_registry.py
>                                                                     └─► build_dashboard.py
> ```
>
> Todo el código del watcher vive en `documentation/setup/syncthing/`. El runbook lo configura una sola vez.

---

## Antes de empezar

- Mac mini con Tailscale corriendo y accesible (ya está, lo usamos para servir las docs).
- Homebrew instalado.
- El repo `documentation/` clonado en el Mac mini. **Decide la ruta y úsala consistentemente** — abajo la llamo `REPO_PATH`. Ejemplo: `/Users/javier/projects/master-healthcare-ai`. El `raw_data/` que sincronizamos es `$REPO_PATH/raw_data/`.

---

## Paso 1 — Instalar Syncthing y fswatch en el Mac mini

```bash
brew install syncthing fswatch

# Lanza Syncthing como servicio del usuario (arranca con el login).
brew services start syncthing

# Verifica:
brew services list | grep syncthing       # debe decir "started"
```

La UI de Syncthing queda en `http://127.0.0.1:8384/` **solo accesible desde localhost por defecto**. No la expongas sin auth.

Si quieres administrarla desde tu portátil sobre Tailnet, abre `~/Library/Application Support/Syncthing/config.xml`, busca `<gui>` y cambia:

```xml
<address>127.0.0.1:8384</address>
```

por

```xml
<address>ais-mac-mini.taild30b92.ts.net:8384</address>
```

Pon un user/password en la misma sección (`<user>` / `<password>`). Reinicia: `brew services restart syncthing`.

---

## Paso 2 — Compartir `raw_data/` desde el Mac mini

1. Abre `http://127.0.0.1:8384/` (o la URL Tailnet si has hecho el paso anterior).
2. **Add Folder**:
   - **Folder Label:** `master-healthcare-ai/raw_data`
   - **Folder ID:** déjalo autogenerado (lo necesitarás abajo).
   - **Folder Path:** `REPO_PATH/raw_data` (la ruta absoluta del Mac mini).
   - **File Versioning:** activa "Staggered File Versioning" — 1 año, mantiene copias de borrados/modificados. **Crítico** para no perder originales.
3. **Ignore Patterns** → pega el contenido de `setup/syncthing/.stignore`.
   - Alternativa: copia el fichero a `REPO_PATH/raw_data/.stignore` y déjalo vacío en la UI; Syncthing lo respeta.
4. Save. La carpeta queda en estado "Idle" sin nadie con quien sincronizar todavía.

---

## Paso 3 — Conectar tu portátil (y/o móvil)

### Portátil (macOS / Windows / Linux)

```bash
brew install syncthing       # o el equivalente en tu OS
brew services start syncthing
```

1. Abre `http://127.0.0.1:8384/` en el portátil.
2. **Actions → Show ID** → copia el Device ID largo.
3. Vuelve al Mac mini, **Add Remote Device**, pega el ID, dale nombre ("portátil-javier"), marca "Auto Accept" si confías en el dispositivo.
4. En el portátil aparecerá una notificación pidiendo aceptar la conexión y la carpeta — acepta ambas y elige dónde guardar `raw_data/` localmente.

### Móvil

- **iOS:** Möbius Sync (de pago, hecho específicamente para Syncthing).
- **Android:** Syncthing oficial (gratis, F-Droid o Play Store).

Mismo flujo: copia el Device ID del móvil, lo añades en el Mac mini, aceptas la carpeta en el móvil. En iOS conviene marcar la carpeta como "Send Only" desde el móvil para que actúe como buzón (subes, no bajas todo el corpus).

---

## Paso 4 — Instalar el watcher (servicio launchd)

```bash
# 1. Asegúrate de que la pipeline funciona a mano:
cd REPO_PATH/documentation
python3 scripts/ingest.py --dry-run
python3 scripts/validate_registry.py

# 2. Da permisos de ejecución al watcher:
chmod +x setup/syncthing/raw-data-watcher.sh

# 3. Prueba el watcher en primer plano (Ctrl-C para parar):
setup/syncthing/raw-data-watcher.sh
#   → deberías ver "watcher arrancando" y luego silencio.
#   → toca un fichero dentro de raw_data/ para ver el evento.

# 4. Cuando estés satisfecho, instala el servicio:
sed "s|__REPO_PATH__|$(pwd)/..|g" \
  setup/syncthing/dev.vinals.master-healthcare-ai.watcher.plist \
  > ~/Library/LaunchAgents/dev.vinals.master-healthcare-ai.watcher.plist

launchctl bootstrap gui/$(id -u) \
  ~/Library/LaunchAgents/dev.vinals.master-healthcare-ai.watcher.plist

# 5. Verifica:
launchctl print gui/$(id -u)/dev.vinals.master-healthcare-ai.watcher | head -20
```

Si todo va bien deberías ver `state = running`.

Logs:

- `setup/syncthing/logs/watcher.log` — eventos detectados, ingestiones lanzadas.
- `setup/syncthing/logs/launchd.{out,err}.log` — stdout/stderr del proceso supervisado.

---

## Paso 5 — Test de extremo a extremo

Desde el **portátil** o **móvil**:

1. Copia un PDF nuevo a la carpeta sincronizada `raw_data/master-training/Formación/test/`.
2. Espera 30–60 s.
3. En el Mac mini:

```bash
tail -f REPO_PATH/documentation/setup/syncthing/logs/watcher.log
```

Deberías ver:

```
evento: .../raw_data/master-training/Formación/test/nuevo.pdf
debounce satisfecho (...)  — disparo ingestión
→ python scripts/ingest.py
→ python scripts/validate_registry.py
→ python scripts/build_dashboard.py
ingestión completada
```

4. Comprueba el registro:

```bash
grep -A2 "nuevo" REPO_PATH/documentation/data/document-registry.yaml
```

5. Comprueba el dashboard:

```bash
head -20 REPO_PATH/documentation/dashboard/README.md
```

---

## Operación normal

- **Subir un documento desde el iPhone:** lo arrastras a la carpeta Möbius Sync de `raw_data/`. Espera. Listo.
- **Subir desde el portátil:** lo copias a tu copia local de `raw_data/`. Syncthing lo propaga. El watcher lo ingiere.
- **Quitar un documento:** **no lo borres directamente** — muévelo dentro de `raw_data/` a una carpeta `archive/` o etiqueta su entrada en el registro como `Archived`. Syncthing tiene versionado activado y lo conservará un año, pero el registro mantiene su historia *para siempre*.

---

## Troubleshooting

| Síntoma | Causa probable | Acción |
|---|---|---|
| Subo un fichero, no pasa nada en el log | El watcher no está corriendo | `launchctl print gui/$(id -u)/dev.vinals.master-healthcare-ai.watcher` — si dice `state = not running`, mira `launchd.err.log` |
| `fswatch: command not found` en el log | PATH no incluye Homebrew | Edita el plist (`EnvironmentVariables → PATH`) y recarga el servicio |
| Ingestión se ejecuta dos veces seguidas con el mismo fichero | Syncthing tocó el mtime tras la primera | Aceptable — la pipeline es idempotente (SHA-256 → skip). Verifica viendo "skip (already ingested)" en `watcher.log` |
| El registro crece pero el dashboard no | `build_dashboard.py` falla — mira `watcher.log` | Probable problema de YAML por edición manual; corre el validador |
| El móvil sincroniza pero se queda en "Out of Sync" | El móvil no es maestro y el watcher tocó algo del lado del Mac (no debería) | El watcher **no escribe** dentro de `raw_data/`, sólo lee. Si pasa, abre incidencia |
| Quiero pausar el watcher temporalmente | — | `launchctl bootout gui/$(id -u)/dev.vinals.master-healthcare-ai.watcher`. Recarga con `bootstrap` cuando termines |
| Quiero ver qué dispositivos están conectados | — | Web UI de Syncthing, sección "Remote Devices" |

---

## Lo que este sistema **no** hace (deliberadamente)

- **No edita los ficheros markdown del repo** (`decisions/`, `meetings/`, etc.). Para eso usaríamos Silverbullet u otro editor — está fuera de scope de esta pieza.
- **No commitea a Git automáticamente.** El watcher actualiza `data/document-registry.yaml` y el dashboard *en el filesystem*, pero el commit lo haces tú (o un cron-job opcional). Esto es deliberado: no queremos que un PDF basura genere un commit a `main` sin revisión.
- **No sincroniza el directorio `documentation/`** en sí. Sólo `raw_data/`. El repo se versiona con Git y se accede vía Tailnet en https://ais-mac-mini.taild30b92.ts.net:5555/.

---

## Una vez funcionando — opcional: auto-commit

Si quieres que cada ingestión genere un commit (recomendable cuando el flujo esté maduro), añade al final de `raw-data-watcher.sh`, dentro de `run_ingest`:

```bash
# Auto-commit de los cambios de registro/dashboard.
(
  cd "$REPO_ROOT"
  if [[ -n "$(git status --porcelain data/document-registry.yaml dashboard/ content/)" ]]; then
    git add data/document-registry.yaml dashboard/ content/
    git commit -m "ingest: auto-commit tras evento de raw_data ($(date '+%Y-%m-%d %H:%M'))"
    # opcional: git push origin main
  fi
) >>"$LOG_FILE" 2>&1 || log "WARN: auto-commit falló"
```

No lo activo de salida — primero quiero verte usar el sistema una semana en modo manual.
