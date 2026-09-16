# my-skills

面向 Claude Code、Codex 以及所有遵循 [Agent Skills](https://agentskills.io) `SKILL.md` 规范的 agent 技能集合。

[English](./README.md)

## 技能列表

| Skill | 作用 |
| --- | --- |
| [`doc-to-markdown`](./skills/doc-to-markdown) | 一条命令把 `.docx`、`.doc`、`.pptx`、`.pdf`、`.epub`、`.xlsx` 转成 Markdown。 |

## 安装

克隆仓库：

```bash
git clone https://github.com/runlinxin-arch/my-skills.git
```

### Claude Code

```bash
cp -R my-skills/skills/doc-to-markdown ~/.claude/skills/
```

也可以用软链接，这样每次 `git pull` 都会同步更新：

```bash
ln -s "$PWD/my-skills/skills/doc-to-markdown" ~/.claude/skills/doc-to-markdown
```

### 其他 agent

任何支持 Agent Skills 格式的 harness 都可以直接用 `skills/doc-to-markdown/SKILL.md`，把该文件指给 agent 即可。

## 初始化

`doc-to-markdown` 依赖 [`markitdown`](https://github.com/microsoft/markitdown) 和几个文档解析库。跑一次脚本装进 skill 自己的虚拟环境：

```bash
bash ~/.claude/skills/doc-to-markdown/scripts/setup.sh
```

脚本会在 skill 目录下创建 `.venv/` 并安装 `requirements.txt`。skill 运行时优先使用这个解释器，找不到就退回系统 `python3`。

虚拟环境**刻意不提交**——它有几百 MB，而且可以完全由 `requirements.txt` 重建。

## 转换文档

```bash
PY=~/.claude/skills/doc-to-markdown/.venv/bin/python
"$PY" ~/.claude/skills/doc-to-markdown/scripts/convert.py 报告.docx 演示.pptx

# OK   报告.docx -> /Users/you/skills/报告.md
# OK   演示.pptx -> /Users/you/skills/演示.md
```

默认输出到 `~/skills`。可以单次覆盖，也可以整段 shell 生效：

```bash
"$PY" .../convert.py 报告.docx --outdir ./out
export DOC2MD_OUTDIR=./out
```

同名文件不会被覆盖，而是自动加序号（`报告.md` → `报告-1.md`），重复执行是安全的。

## 支持的格式

| 格式 | 说明 |
| --- | --- |
| `.docx` | 标题层级、表格、列表都能保留。 |
| `.pptx` | 按页提取幻灯片文字。 |
| `.pdf` | 需要文字层。扫描版 PDF（纯图片）转出来是空的，得先做 OCR。 |
| `.epub` | 章节转成 Markdown。 |
| `.xlsx` | 工作表数据转成表格。 |
| `.doc` | 老式二进制格式，支持有限。失败的话先另存为 `.docx`。 |

## 评测

`skills/doc-to-markdown/evals/` 存放评测集和测试文件：

```bash
python3 skills/doc-to-markdown/evals/make_fixtures.py   # 重新生成测试文件
```

`evals.json` 描述了三组「触发 + 输出」用例，用来验证 skill 能否在文档转换请求上正确触发并产出可用的 Markdown。

## 许可

[MIT](./LICENSE)
