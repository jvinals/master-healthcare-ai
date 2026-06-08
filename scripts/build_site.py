#!/usr/bin/env python3
"""Prepara ``website/docs/`` con symlinks a los directorios publicables y
ejecuta ``mkdocs build``.

MkDocs exige que ``docs_dir`` sea un sub-directorio del directorio que
contiene ``mkdocs.yml``. Como nuestros markdown viven en
``curriculum/``, ``dashboard/``, ``content/``, etc. en la raíz del repo
(porque son tanto contenido publicable como artefacto de gobernanza), no
podemos apuntar ``docs_dir`` directamente a ellos. Solución: rellenamos
``website/docs/`` con symlinks justo antes de cada build.

Uso:

    python scripts/build_site.py            # build estático -> website/site/
    python scripts/build_site.py --serve    # mkdocs serve en local
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DOC_ROOT = SCRIPT_DIR.parent
WEB_ROOT = DOC_ROOT / "website"
DOCS_DIR = WEB_ROOT / "docs"

# (source relative to DOC_ROOT, link path relative to DOCS_DIR)
PUBLISH_MAP = [
    ("README.md", "index.md"),
    ("CONTRIBUTING.md", "contribuir.md"),
    ("CONTRIBUTING.md", "CONTRIBUTING.md"),  # keep original link target alive too
    ("roadmap.md", "roadmap.md"),
    ("curriculum", "curriculum"),
    ("modules", "modules"),
    ("activities", "activities"),
    ("assessments", "assessments"),
    ("faculty", "faculty"),
    ("administration", "administration"),
    ("meetings", "meetings"),
    ("decisions", "decisions"),
    ("research", "research"),
    ("requirements", "requirements"),
    ("timeline", "timeline"),
    ("dashboard", "dashboard"),
    ("content", "content"),
    ("wiki", "wiki"),
    ("templates", "templates"),
]


def prepare() -> None:
    if DOCS_DIR.exists():
        # Wipe to avoid stale links pointing nowhere.
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir(parents=True)

    for src_rel, dst_rel in PUBLISH_MAP:
        src = DOC_ROOT / src_rel
        if not src.exists():
            continue
        dst = DOCS_DIR / dst_rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        # Relative symlink so the tree is portable.
        rel = os.path.relpath(src, dst.parent)
        os.symlink(rel, dst)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--serve", action="store_true",
                        help="Lanza 'mkdocs serve' en lugar de build.")
    parser.add_argument("--strict", action="store_true",
                        help="Falla ante warnings de MkDocs.")
    args = parser.parse_args()

    prepare()
    cmd = ["mkdocs", "serve" if args.serve else "build", "-f", str(WEB_ROOT / "mkdocs.yml")]
    if args.strict and not args.serve:
        cmd.append("--strict")
    print(">>>", " ".join(cmd))
    return subprocess.call(cmd)


if __name__ == "__main__":
    sys.exit(main())
