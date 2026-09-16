# my-skills

Agent Skills for Claude Code, Codex, and any harness that follows the [Agent Skills](https://agentskills.io) `SKILL.md` convention.

[中文说明](./README.zh-CN.md)

## Skills

| Skill | What it does |
| --- | --- |
| [`doc-to-markdown`](./skills/doc-to-markdown) | Convert `.docx`, `.doc`, `.pptx`, `.pdf`, `.epub`, and `.xlsx` files to Markdown in one command. |

## Install

Clone the repository:

```bash
git clone https://github.com/runlinxin-arch/my-skills.git
```

### Claude Code

```bash
cp -R my-skills/skills/doc-to-markdown ~/.claude/skills/
```

Symlinking works too, and keeps the skill updated on every `git pull`:

```bash
ln -s "$PWD/my-skills/skills/doc-to-markdown" ~/.claude/skills/doc-to-markdown
```

### Other agents

Any harness that reads the Agent Skills format can use `skills/doc-to-markdown/SKILL.md` directly — point it at that file and it will load the skill.

## Setup

`doc-to-markdown` depends on [`markitdown`](https://github.com/microsoft/markitdown) plus a few document parsers. Install them into the skill's own virtualenv once:

```bash
bash ~/.claude/skills/doc-to-markdown/scripts/setup.sh
```

The script creates `.venv/` inside the skill directory and installs `requirements.txt`. The skill prefers that interpreter and falls back to the system `python3` when it is absent.

The virtualenv is deliberately **not** committed — it is several hundred megabytes and is fully reproducible from `requirements.txt`.

## Convert a document

```bash
PY=~/.claude/skills/doc-to-markdown/.venv/bin/python
"$PY" ~/.claude/skills/doc-to-markdown/scripts/convert.py report.docx slides.pptx

# OK   report.docx -> /Users/you/skills/report.md
# OK   slides.pptx -> /Users/you/skills/slides.md
```

Output goes to `~/skills` by default. Override it per run or per shell:

```bash
"$PY" .../convert.py report.docx --outdir ./out
export DOC2MD_OUTDIR=./out
```

Existing files are never overwritten — a numeric suffix is appended instead (`report.md` → `report-1.md`), so re-running is safe.

## Supported formats

| Format | Notes |
| --- | --- |
| `.docx` | Headings, tables, and lists preserved. |
| `.pptx` | Slide text extracted per slide. |
| `.pdf` | Needs a text layer. Scanned PDFs (images only) come out empty — run OCR first. |
| `.epub` | Chapters converted to Markdown. |
| `.xlsx` | Sheet data converted to tables. |
| `.doc` | Legacy binary format; support is limited. Re-save as `.docx` if it fails. |

## Evals

`skills/doc-to-markdown/evals/` holds the eval set and its fixtures:

```bash
python3 skills/doc-to-markdown/evals/make_fixtures.py   # regenerate fixtures
```

`evals.json` describes the three trigger-and-output cases used to check that the skill fires on document-conversion requests and produces usable Markdown.

## License

[MIT](./LICENSE)
