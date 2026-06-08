#!/usr/bin/env python3
"""Genera ``dashboard/README.md`` y ``dashboard/families.md`` a partir del registro."""
from __future__ import annotations

import datetime as dt
from collections import Counter, defaultdict
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
DOC_ROOT = SCRIPT_DIR.parent
REGISTRY = DOC_ROOT / "data" / "document-registry.yaml"
DASH_DIR = DOC_ROOT / "dashboard"


def main() -> int:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    docs = data.get("documents", [])
    DASH_DIR.mkdir(parents=True, exist_ok=True)

    total = len(docs)
    by_status = Counter(d.get("status", "Draft") for d in docs)
    by_category = Counter(d.get("category", "otros") for d in docs)
    by_lang = Counter(d.get("language", "es") for d in docs)
    canon = sum(1 for d in docs if d.get("canonical"))
    families = defaultdict(list)
    for d in docs:
        families[d.get("family_id", "")].append(d)
    multi_fam = {f: ms for f, ms in families.items() if len(ms) > 1}

    now = dt.datetime.now().isoformat(timespec="seconds")

    lines: list[str] = []
    lines.append("# Dashboard\n")
    lines.append(f"_Última generación: {now}_\n")

    lines.append("## Resumen\n")
    lines.append("| Métrica | Valor |")
    lines.append("|---|---|")
    lines.append(f"| Documentos registrados | {total} |")
    lines.append(f"| Documentos canónicos | {canon} |")
    lines.append(f"| Familias de versiones | {len(families)} |")
    lines.append(f"| Familias con varias versiones | {len(multi_fam)} |")
    lines.append("")

    lines.append("## Por estado\n")
    lines.append("| Estado | Documentos |")
    lines.append("|---|---|")
    for status, n in sorted(by_status.items(), key=lambda x: -x[1]):
        lines.append(f"| {status} | {n} |")
    lines.append("")

    lines.append("## Por categoría\n")
    lines.append("| Categoría | Documentos |")
    lines.append("|---|---|")
    for cat, n in sorted(by_category.items(), key=lambda x: -x[1]):
        lines.append(f"| {cat} | {n} |")
    lines.append("")

    lines.append("## Por idioma\n")
    lines.append("| Idioma | Documentos |")
    lines.append("|---|---|")
    for lang, n in sorted(by_lang.items(), key=lambda x: -x[1]):
        lines.append(f"| {lang} | {n} |")
    lines.append("")

    lines.append("## Familias con múltiples versiones\n")
    lines.append("Cada fila es una familia. Conviene revisarlas y marcar **una** versión como `canonical: true` "
                 "(ver `data/document-registry.yaml`).\n")
    lines.append("| Familia | Miembros | Canónico actual |")
    lines.append("|---|---|---|")
    for fam, ms in sorted(multi_fam.items()):
        canonical = ", ".join(m["id"] for m in ms if m.get("canonical")) or "_(ninguno)_"
        members = ", ".join(sorted(m["id"] for m in ms))
        lines.append(f"| `{fam}` | {members} | {canonical} |")
    lines.append("")
    lines.append("Detalle por familia: [`families.md`](families.md).\n")

    lines.append("## Últimos cambios (registro)\n")
    recent = sorted(docs, key=lambda d: d.get("updated", ""), reverse=True)[:20]
    lines.append("| Actualizado | ID | Título | Estado | Canónico |")
    lines.append("|---|---|---|---|---|")
    for d in recent:
        lines.append(
            f"| {d.get('updated','')} | {d.get('id','')} | {d.get('title','')[:60]} "
            f"| {d.get('status','')} | {'sí' if d.get('canonical') else ''} |"
        )

    (DASH_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # families.md — detail
    fam_lines: list[str] = ["# Familias de versiones\n",
                            f"_Última generación: {now}_\n"]
    for fam, ms in sorted(families.items()):
        fam_lines.append(f"## `{fam}`\n")
        fam_lines.append("| ID | Versión | Estado | Canónico | Actualizado | Title |")
        fam_lines.append("|---|---|---|---|---|---|")
        for m in sorted(ms, key=lambda x: x.get("version", "")):
            fam_lines.append(
                f"| {m.get('id','')} | {m.get('version','')} | {m.get('status','')} "
                f"| {'sí' if m.get('canonical') else ''} | {m.get('updated','')} "
                f"| {m.get('title','')[:70]} |"
            )
        fam_lines.append("")
    (DASH_DIR / "families.md").write_text("\n".join(fam_lines) + "\n", encoding="utf-8")

    print(f"dashboard escrito ({total} docs, {len(families)} familias).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
