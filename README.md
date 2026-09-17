# file-to-markdown

Convert `.docx`, `.doc`, `.pptx`, `.pdf`, `.epub`, and `.xlsx` files to Markdown in one command. Works with Claude Code, Codex, and any harness that follows the [Agent Skills](https://agentskills.io) `SKILL.md` convention.

English | [中文](#中文)

## Install

Clone the repository:

```bash
git clone https://github.com/runlinxin-arch/file-to-markdown.git
```

### Claude Code

```bash
cp -R file-to-markdown/skills/file-to-markdown ~/.claude/skills/
```

Symlinking works too, and keeps the skill updated on every `git pull`:

```bash
ln -s "$PWD/file-to-markdown/skills/file-to-markdown" ~/.claude/skills/file-to-markdown
```

### Other agents

Any harness that reads the Agent Skills format can use `skills/file-to-markdown/SKILL.md` directly — point it at that file and it will load the skill.

## Dependencies

Copying the files is the whole install — there is no build step. `file-to-markdown` depends only on [`markitdown`](https://github.com/microsoft/markitdown) (with all format-parser extras). If the first conversion reports a missing dependency, install it once into your Python environment:

```bash
python -m pip install "markitdown[all]"
```

With [uv](https://docs.astral.sh/uv/) you can skip touching the system environment entirely:

```bash
uv run --with "markitdown[all]" .../convert.py report.docx
```

## Convert a document

```bash
python ~/.claude/skills/file-to-markdown/scripts/convert.py report.docx slides.pptx

# OK   report.docx -> /Users/you/skills/report.md
# OK   slides.pptx -> /Users/you/skills/slides.md
```

Output goes to `~/skills` by default. Override it per run or per shell:

```bash
python .../convert.py report.docx --outdir ./out
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

`skills/file-to-markdown/evals/` holds the eval set and its fixtures:

```bash
python3 skills/file-to-markdown/evals/make_fixtures.py   # regenerate fixtures
```

`evals.json` describes the three trigger-and-output cases used to check that the skill fires on document-conversion requests and produces usable Markdown.

## License

[MIT](./LICENSE)

---

## 中文

一条命令把 `.docx`、`.doc`、`.pptx`、`.pdf`、`.epub`、`.xlsx` 转成 Markdown。面向 Claude Code、Codex 以及所有遵循 [Agent Skills](https://agentskills.io) `SKILL.md` 规范的 agent。

### 安装

克隆仓库：

```bash
git clone https://github.com/runlinxin-arch/file-to-markdown.git
```

#### Claude Code

```bash
cp -R file-to-markdown/skills/file-to-markdown ~/.claude/skills/
```

也可以用软链接，这样每次 `git pull` 都会同步更新：

```bash
ln -s "$PWD/file-to-markdown/skills/file-to-markdown" ~/.claude/skills/file-to-markdown
```

#### 其他 agent

任何支持 Agent Skills 格式的 harness 都可以直接用 `skills/file-to-markdown/SKILL.md`，把该文件指给 agent 即可。

### 依赖

复制即完成安装，没有构建步骤。`file-to-markdown` 只依赖 [`markitdown`](https://github.com/microsoft/markitdown)（含全部格式解析 extras）。首次转换时如果当前 Python 环境缺依赖，装一次即可（全局有效）：

```bash
python -m pip install "markitdown[all]"
```

装了 [uv](https://docs.astral.sh/uv/) 的机器可以不污染系统环境：

```bash
uv run --with "markitdown[all]" .../convert.py 报告.docx
```

### 转换文档

```bash
python ~/.claude/skills/file-to-markdown/scripts/convert.py 报告.docx 演示.pptx

# OK   报告.docx -> /Users/you/skills/报告.md
# OK   演示.pptx -> /Users/you/skills/演示.md
```

默认输出到 `~/skills`。可以单次覆盖，也可以整段 shell 生效：

```bash
python .../convert.py 报告.docx --outdir ./out
export DOC2MD_OUTDIR=./out
```

同名文件不会被覆盖，而是自动加序号（`报告.md` → `报告-1.md`），重复执行是安全的。

### 支持的格式

| 格式 | 说明 |
| --- | --- |
| `.docx` | 标题层级、表格、列表都能保留。 |
| `.pptx` | 按页提取幻灯片文字。 |
| `.pdf` | 需要文字层。扫描版 PDF（纯图片）转出来是空的，得先做 OCR。 |
| `.epub` | 章节转成 Markdown。 |
| `.xlsx` | 工作表数据转成表格。 |
| `.doc` | 老式二进制格式，支持有限。失败的话先另存为 `.docx`。 |

### 评测

`skills/file-to-markdown/evals/` 存放评测集和测试文件：

```bash
python3 skills/file-to-markdown/evals/make_fixtures.py   # 重新生成测试文件
```

`evals.json` 描述了三组「触发 + 输出」用例，用来验证 skill 能否在文档转换请求上正确触发并产出可用的 Markdown。

### 许可

[MIT](./LICENSE)
