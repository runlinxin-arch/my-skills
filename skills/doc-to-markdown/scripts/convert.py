#!/usr/bin/env python3
"""Convert documents (docx, pptx, pdf, epub, xlsx, ...) to Markdown.

Usage:
    convert.py <input-file> [<input-file> ...] [--outdir DIR]

Each input file is converted with markitdown and written as
<outdir>/<original-basename>.md. Existing files are not overwritten;
a numeric suffix is appended instead.

The output directory defaults to $DOC2MD_OUTDIR when that is set, and to
~/skills otherwise.
"""

import argparse
import os
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

try:
    from markitdown import MarkItDown
except ImportError:
    sys.exit(
        "markitdown is not installed for this interpreter.\n"
        "Run scripts/setup.sh once to create the skill's virtualenv, or install\n"
        "the dependencies manually:  python3 -m pip install -r requirements.txt"
    )

DEFAULT_OUTDIR = Path(
    os.environ.get("DOC2MD_OUTDIR") or Path.home() / "skills"
).expanduser()


def output_path_for(src: Path, outdir: Path) -> Path:
    candidate = outdir / (src.stem + ".md")
    n = 1
    while candidate.exists():
        candidate = outdir / f"{src.stem}-{n}.md"
        n += 1
    return candidate


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert documents to Markdown.")
    parser.add_argument("inputs", nargs="+", type=Path, help="files to convert")
    parser.add_argument("--outdir", type=Path, default=DEFAULT_OUTDIR,
                        help=f"output directory (default: {DEFAULT_OUTDIR})")
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)
    converter = MarkItDown()
    failures = 0

    for src in args.inputs:
        if not src.is_file():
            print(f"SKIP {src}: not a file", file=sys.stderr)
            failures += 1
            continue
        try:
            result = converter.convert(str(src))
        except Exception as exc:
            print(f"FAIL {src}: {exc}", file=sys.stderr)
            failures += 1
            continue
        dest = output_path_for(src, args.outdir)
        dest.write_text(result.text_content, encoding="utf-8")
        print(f"OK   {src} -> {dest}")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
