"""Post-pass: fix categories for the canonical PDF + sibling Micromódulo files,
and mark the canonical PDF as Published/canonical so we have at least one anchor."""
from pathlib import Path
import unicodedata
import yaml

reg_path = Path(__file__).resolve().parent.parent / "data" / "document-registry.yaml"
data = yaml.safe_load(reg_path.read_text(encoding="utf-8"))

fixes = 0
for d in data["documents"]:
    src = (d.get("source_file") or "")
    src_ascii = unicodedata.normalize("NFKD", src).encode("ascii", "ignore").decode("ascii").lower()
    if d.get("category") == "otros" and "micromodulo" in src_ascii:
        d["category"] = "micromodulo-ia-salud"
        fixes += 1

# Anchor: the canonical micromódulo PDF
for d in data["documents"]:
    if d["id"] == "DOC-0035":
        d["canonical"] = True
        d["status"] = "Published"
        d["version"] = "1.0"
        d["author"] = "Vinals, Francisco Javier"
        d["tags"] = sorted(set((d.get("tags") or []) + ["micromodulo", "ia", "salud", "canonico"]))
        fam_id = d["family_id"]
        data["families"].setdefault(fam_id, {"members": [], "canonical": None})
        data["families"][fam_id]["canonical"] = d["id"]

reg_path.write_text(
    "# Registro canónico de documentos. Generado por scripts/ingest.py.\n"
    "# La revisión humana decide canonical/status/family_id finales.\n\n"
    + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100),
    encoding="utf-8",
)
print(f"category fixes: {fixes}; canonical PDF DOC-0035 marked.")
