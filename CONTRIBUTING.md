# Guía de contribución y gobernanza documental

Este documento define las **reglas no negociables** del repositorio. Todo cambio debe respetarlas.

---

## 1. Principios

1. **Nunca se sobrescribe.** Toda versión anterior se preserva.
2. **Nunca se borra.** Los obsoletos se mueven a `archive/`, no a la papelera.
3. **Toda decisión debe ser rastreable.** Cambio → decisión → reunión → faculty/admin que lo aprobó.
4. **Markdown primero.** El formato canónico de cualquier contenido editable es markdown con frontmatter YAML.
5. **El registro manda.** `data/document-registry.yaml` es la fuente de verdad sobre qué es canónico.

---

## 2. Frontmatter obligatorio

Todo archivo markdown bajo `content/`, `modules/`, `activities/`, `assessments/`, `faculty/`, `meetings/`, `decisions/`, `requirements/` y `curriculum/` debe empezar con:

```yaml
---
id: ID-UNICO-CORTO              # p.ej. DOC-0042, MOD-03, DEC-2026-006
title: Título humano del documento
version: "1.0"                  # SemVer-lite: mayor.menor[.parche]
status: Draft                   # Draft | Under Review | Approved | Published | Archived | Superseded
authors:                        # lista
  - "Apellido, Nombre"
created: 2026-06-08             # ISO 8601 (YYYY-MM-DD)
updated: 2026-06-08
tags:                           # lista de etiquetas en minúsculas
  - curriculum
  - modulo-1
related:                        # lista de IDs de otros documentos
  - DOC-0007
source: raw_data/...            # ruta relativa al original (si aplica)
source_sha256: ""               # hash del fichero fuente (rellenado por la ingestión)
canonical: false                # sólo UNO por familia puede ser true
family_id: ""                   # agrupa versiones del mismo artefacto
supersedes: []                  # lista de IDs que este documento reemplaza
superseded_by: ""               # ID que reemplaza a éste, si aplica
language: es
---
```

Cualquier campo añadido (p.ej. `module_number`, `ects`, `competencias`) es bienvenido si añade información estructurada y reutilizable.

---

## 3. Estados permitidos

| Estado | Significado |
|---|---|
| `Draft` | Borrador. No representa una posición acordada. |
| `Under Review` | En revisión por faculty o administración. |
| `Approved` | Aprobado pero aún no publicado. |
| `Published` | Aprobado y publicado (puede ser canónico). |
| `Archived` | Obsoleto pero conservado. |
| `Superseded` | Reemplazado por otra versión más reciente. |

Transiciones válidas: `Draft → Under Review → Approved → Published → (Superseded | Archived)`. Saltarse pasos requiere justificación en la decisión correspondiente.

---

## 4. Versionado

- `mayor.menor[.parche]`.
- **Mayor:** cambios estructurales (módulos añadidos/eliminados, reorganización del programa, cambio de objetivos).
- **Menor:** revisiones de contenido sustantivas.
- **Parche:** correcciones, ortografía, refactor de presentación.
- Cualquier cambio que altere significado académico debe documentarse en `changes/<id>.md`.

---

## 5. Convenciones de nombrado de ficheros

- Carpeta: minúsculas, guiones (`activities/modulo-3-laboratorio-prompting.md`).
- ID: tres letras + guion + número con ceros a la izquierda. Familias de IDs reservadas:
  - `DOC-####` documentos genéricos
  - `MOD-##` módulos
  - `ACT-####` actividades
  - `ASM-####` evaluaciones
  - `FAC-###` faculty
  - `MEET-YYYY-MM-DD-###` reuniones
  - `DEC-YYYY-###` decisiones
  - `REQ-####` requisitos
- Nunca usar `final`, `final2`, `definitivo` en el nombre. Si es la versión actual lo dice `canonical: true`.

---

## 6. Familias de versiones

Un mismo artefacto académico (p.ej. "ANEXO I Propuesta de Título") puede existir en múltiples ficheros. Se agrupan con `family_id`:

```
family_id: "anexo-i-propuesta-titulo"

# v1 (Dic 2023)
id: DOC-0011, version: "1.0", canonical: false, superseded_by: DOC-0012

# v2 (revisión JV)
id: DOC-0012, version: "1.1", canonical: false, supersedes: [DOC-0011], superseded_by: DOC-0013

# v3 (entregada)
id: DOC-0013, version: "2.0", canonical: true, supersedes: [DOC-0012]
```

El script `scripts/ingest.py` propone `family_id` automáticamente a partir del nombre de fichero normalizado; debe ser revisado por una persona.

---

## 7. Decisiones (ADR)

Toda decisión sustantiva vive en `decisions/DEC-YYYY-###-titulo-corto.md` con frontmatter mínimo:

```yaml
---
id: DEC-2026-006
title: Aprobar v2.0 del ANEXO I como versión canónica
date: 2026-06-08
status: Accepted          # Proposed | Accepted | Rejected | Superseded
deciders:
  - "Vinals, Javier"
meeting: MEET-2026-06-05-001    # opcional
affects:
  - DOC-0011
  - DOC-0012
  - DOC-0013
---
```

Cuerpo libre: contexto, alternativas consideradas, decisión, consecuencias.

---

## 8. Workflow de cambio típico

```
1. Aparece fichero nuevo en raw_data/
2. python scripts/ingest.py
   → genera content/<slug>.md
   → añade entrada provisional al registro (status: Draft, canonical: false)
3. Una persona revisa:
   - corrige metadatos
   - decide family_id
   - escribe decisión en decisions/ si procede
   - cambia status según corresponda
   - si es nueva versión canónica: marca canonical: true y mueve la anterior
4. python scripts/validate_registry.py   # debe pasar
5. python scripts/build_dashboard.py
6. git commit -m "doc(<id>): <título>"
7. git push
```

---

## 9. Herramientas

| Comando | Para qué |
|---|---|
| `python scripts/ingest.py` | Escanea `raw_data/`, ingiere ficheros nuevos, actualiza registro. |
| `python scripts/validate_registry.py` | Valida invariantes del registro (1 canónico por familia, sin IDs duplicados, etc.). |
| `python scripts/build_dashboard.py` | Regenera `dashboard/README.md`. |
| `mkdocs serve` | Sirve el sitio en local. |
| `mkdocs build` | Construye el sitio estático. |

---

## 10. Lo que **no** se hace

- No se edita el contenido de `archive/` salvo metadatos.
- No se cambia un ID una vez asignado.
- No se borra una entrada del registro; se marca `Archived` o `Superseded`.
- No se commits archivos binarios pesados sin justificación (los originales viven en `raw_data/`, no en este repo).
- No se introducen dependencias del sitio (Next.js, pgvector) sin una decisión formal.
