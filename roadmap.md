# Roadmap

> Estado vivo. Se actualiza cuando algo se completa, se mueve o se bloquea. Cada ítem debería poder enlazar a una decisión o reunión.

## Completado

- [x] **Bootstrap del repositorio** (2026-06-08) — estructura, README, CONTRIBUTING, registro inicial, script de ingestión, dashboard mínimo, sitio MkDocs base.
- [x] **Ingestión inicial** — `raw_data/master-training/` escaneado completo; cada fichero entra en `content/` y en `data/document-registry.yaml` como `Draft`.

## En curso

- [ ] **Revisión humana del registro** — un responsable debe recorrer `data/document-registry.yaml` y:
  - Confirmar o corregir cada `family_id` propuesto.
  - Marcar el `canonical: true` correcto por familia.
  - Ajustar `status` según realidad académica/administrativa.
- [ ] **Extracción del esqueleto curricular del PDF canónico** — modulos, objetivos, competencias, resultados de aprendizaje pasan de `content/microm*.md` a páginas estructuradas en `curriculum/` y `modules/`.

## Planificado

- [ ] **Decisiones retroactivas** — para cada cambio de versión histórico (p.ej. v1.0 → v1.1 del ANEXO I), abrir un ADR en `decisions/` aunque la decisión sea pasada, para reconstruir trazabilidad.
- [ ] **Timeline reconstruido** — generar `timeline/README.md` a partir de fechas `created`/`updated` del registro y reuniones registradas.
- [ ] **Knowledge graph** — `data/knowledge-graph.yaml` con relaciones módulo↔actividad, faculty↔módulo, decisión↔documento. Render Mermaid.
- [ ] **CI mínimo** — GitHub Action que ejecute `validate_registry.py` y `mkdocs build` en cada push.
- [ ] **Plantillas** — `templates/` con esqueletos para módulo, actividad, evaluación, ADR, reunión.
- [ ] **Búsqueda mejorada** — evaluar si la búsqueda built-in de MkDocs basta o si conviene añadir un índice semántico ligero (sentence-transformers local, sin pgvector).

## Bloqueado / requiere input

- [ ] **Confirmar autoría académica del Micromódulo** (¿sólo JV? ¿co-autores?) — necesario para rellenar `authors:` correctamente.
- [ ] **Lista de stakeholders y aprobadores en UCJC** — necesario para `decisions/` reales.
- [ ] **¿Se publica el sitio?** Si sí, decidir si va a GitHub Pages, dominio propio, o sólo se sirve interno.

## No haremos (decisión explícita)

- Next.js + Tailwind + MDX como sitio público — sobre-ingeniería para el caso actual.
- pgvector + OpenAI Embeddings — la búsqueda built-in basta hasta que haya evidencia de necesidad.
- Ingestión OCR — los ficheros disponibles son texto digital; OCR sólo si aparecen escaneos.
