# Micromódulo de Formación Permanente en Inteligencia Artificial para la Salud — Documentación

Repositorio de **memoria institucional** del programa. Punto único de verdad para currículum, decisiones, faculty, administración, evaluaciones y trazabilidad histórica de cada documento.

> **Regla de oro:** nunca se sobrescribe ni se borra. Toda versión anterior se conserva, se enlaza y se archiva. El registro canónico vive en `data/document-registry.yaml`.

---

## Mapa rápido

| Carpeta | Para qué sirve |
|---|---|
| `content/` | Markdown normalizado de todos los documentos ingeridos. Una página por documento, con frontmatter completo. |
| `curriculum/` | Visión, objetivos, competencias, resultados de aprendizaje. Estructura académica del programa. |
| `modules/` | Una página por módulo académico. |
| `activities/` | Actividades, ejercicios, laboratorios, proyectos. |
| `assessments/` | Evaluaciones, rúbricas, exámenes. |
| `faculty/` | Perfiles de profesorado, responsabilidades, CVs. |
| `administration/` | Presupuestos, stakeholders, contratos, convenios, riesgos. |
| `meetings/` | Actas y notas de reunión. |
| `decisions/` | Decisiones formales (ADR-style). Una decisión = un archivo. |
| `research/` | Referencias, papers, fuentes externas. |
| `requirements/` | Requisitos (académicos, técnicos, administrativos). |
| `timeline/` | Cronología del proyecto: hitos, entregables, aprobaciones, cambios. |
| `changes/` | Changelogs generados (por documento y globales). |
| `wiki/` | Páginas wiki temáticas con backlinks. |
| `dashboard/` | Métricas, contadores, vistas de estado generadas. |
| `archive/` | Versiones obsoletas. Nunca se borran; sólo se mueven aquí. |
| `data/` | Registros estructurados: `document-registry.yaml`, `knowledge-graph.yaml`, etc. |
| `scripts/` | Herramientas: ingestión, validación, regeneración de dashboard. |
| `ingestion/` | Logs y artefactos intermedios de cada pasada de ingestión. |
| `templates/` | Plantillas para crear documentos nuevos respetando el frontmatter. |
| `website/` | Sitio publicable (MkDocs Material). |
| `.github/workflows/` | CI: validación de registro, build del sitio, link-check. |

---

## Cómo navegar

- **¿Qué versión es la actual?** Mira `data/document-registry.yaml` y filtra por `canonical: true`.
- **¿Qué cambió?** Mira `changes/` o el historial Git.
- **¿Por qué cambió?** Cada cambio debería enlazar a una decisión en `decisions/` y, si aplica, a una reunión en `meetings/`.
- **¿Dónde está el original?** El campo `source_file` del registro apunta al fichero crudo en `raw_data/`.
- **¿Qué documentos forman parte de la misma familia de versiones?** El campo `family_id` los agrupa y `supersedes` / `superseded_by` reconstruye la cadena.

---

## Flujo de trabajo (resumen)

1. Aparece un documento nuevo en `raw_data/`.
2. Se ejecuta `python scripts/ingest.py` (ver `CONTRIBUTING.md`).
3. La ingestión:
   - Extrae texto y metadatos.
   - Genera markdown en `content/` con frontmatter.
   - Detecta familia de versiones por similitud de nombre.
   - Inserta o actualiza la entrada en `data/document-registry.yaml`.
4. Una persona revisa el documento, marca `status`, decide si es `canonical`, y enlaza la decisión correspondiente en `decisions/`.
5. Si supersede una versión anterior, ésta se mueve a `archive/` y se actualiza `superseded_by`.
6. Se regenera el dashboard: `python scripts/build_dashboard.py`.

Detalle completo en [`CONTRIBUTING.md`](CONTRIBUTING.md) (en el sitio web: [Reglas y contribución](contribuir.md)).

---

## Estado actual

Ver [`roadmap.md`](roadmap.md) y [`dashboard/README.md`](dashboard/README.md).

---

## Documento canónico de partida

`raw_data/master-training/Formación/Micromódulo en IA para la Salud/Micromódulo de Formación Permanente en Inteligencia Artificial para la salud.pdf`

Es la fuente académica de referencia hasta que se apruebe formalmente una versión posterior.
