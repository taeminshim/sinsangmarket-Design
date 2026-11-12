"""스킬 파일(dist/sinsangmarket-design.skill)을 만든다.

skill/sinsangmarket-design/SKILL.md 와 저장소 문서(README·libraries·design-system·builder)를
references/ 로 묶는다. 문서 원본은 저장소 한 곳에만 두고, 스킬은 이 스크립트로 만든다.

    python3 scripts/build_skill.py
"""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent.parent
NAME = "sinsangmarket-design"
SKILL_MD = ROOT / "skill" / NAME / "SKILL.md"
DOCS = ["README.md", "libraries.md", "design-system", "builder"]
OUT = ROOT / "dist" / f"{NAME}.skill"


def doc_files():
    for doc in DOCS:
        path = ROOT / doc
        if path.is_dir():
            yield from sorted(p for p in path.rglob("*.md"))
        else:
            yield path


def main():
    OUT.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(SKILL_MD, f"{NAME}/SKILL.md")
        for f in doc_files():
            zf.write(f, f"{NAME}/references/{f.relative_to(ROOT).as_posix()}")
    print(f"만들었어요: {OUT.relative_to(ROOT)}")
    for name in zipfile.ZipFile(OUT).namelist():
        print("  ", name)


if __name__ == "__main__":
    main()
