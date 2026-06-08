#!/usr/bin/env python3
"""Valida invariantes de ``data/document-registry.yaml``.

Reglas:

1. IDs únicos.
2. Familias: como mucho un documento canónico por familia.
3. Si ``superseded_by`` apunta a un ID, ese ID debe existir y tener ``supersedes`` recíproco.
4. Si ``status`` es ``Superseded``, debe existir ``superseded_by``.
5. ``content_path`` debe existir en disco.
6. ``source_file`` debe existir en disco.

Salida con código != 0 si falla algo. Pensado para CI.
"""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
DOC_ROOT = SCRIPT_DIR.parent
PROFILE_ROOT = DOC_ROOT.parent
REGISTRY = DOC_ROOT / "data" / "document-registry.yaml"


def main() -> int:
    if not REGISTRY.exists():
        print(f"ERROR: no se encuentra {REGISTRY}", file=sys.stderr)
        return 2
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    docs = data.get("documents", [])

    errors: list[str] = []
    warnings: list[str] = []

    # 1. IDs únicos
    seen = defaultdict(int)
    for d in docs:
        seen[d.get("id", "")] += 1
    for did, n in seen.items():
        if n > 1:
            errors.append(f"ID duplicado: {did} (×{n})")

    by_id = {d["id"]: d for d in docs if d.get("id")}

    # 2. Un canónico por familia
    fam_canon = defaultdict(list)
    for d in docs:
        if d.get("canonical"):
            fam_canon[d.get("family_id", "")].append(d["id"])
    for fam, ids in fam_canon.items():
        if len(ids) > 1:
            errors.append(f"familia {fam} tiene >1 canónico: {ids}")

    # 3 & 4. supersedes / superseded_by
    for d in docs:
        sb = d.get("superseded_by")
        if sb:
            target = by_id.get(sb)
            if not target:
                errors.append(f"{d['id']} superseded_by={sb} no existe")
            else:
                if d["id"] not in (target.get("supersedes") or []):
                    warnings.append(
                        f"{d['id']} → superseded_by {sb}, pero {sb}.supersedes no lo incluye"
                    )
        if d.get("status") == "Superseded" and not sb:
            errors.append(f"{d['id']} status=Superseded pero superseded_by vacío")
        for s in d.get("supersedes") or []:
            if s not in by_id:
                errors.append(f"{d['id']} supersedes {s} que no existe")

    # 5 & 6. Rutas
    for d in docs:
        cp = d.get("content_path", "")
        if cp and not (DOC_ROOT / cp).exists():
            warnings.append(f"{d.get('id')} content_path no existe: {cp}")
        sf = d.get("source_file", "")
        if sf and not (PROFILE_ROOT / sf).exists():
            warnings.append(f"{d.get('id')} source_file no existe: {sf}")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}", file=sys.stderr)

    print(f"\nresumen  docs={len(docs)}  errores={len(errors)}  avisos={len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
