---
name: file-to-markdown
description: 把 docx、word、pptx、PDF、epub 电子书、xlsx 等文档转换成 Markdown，统一输出到 ~/skills。只要用户拖入或提到这类文件、并想把它们转成 markdown / 提取文字内容 / 读取文档内容，就一定要用这个 skill，即使用户没有明说"转换"。内置转换脚本，直接调用即可，不要自己临时写转换代码。Use when converting .docx/.doc/.pptx/.pdf/.epub/.xlsx files to Markdown or extracting their text content.
---

# file-to-markdown

把办公文档和电子书转成 Markdown。支持：`.docx`、`.doc`（word 文档）、`.pptx`、`.pdf`、`.epub`、`.xlsx`。

## 用法

本 skill 无需安装步骤，复制到 skills 目录即可用。转换命令（`<skill>` 指本 skill 所在目录）：

```bash
python "<skill>/scripts/convert.py" <文件路径> [更多文件...]
```

依赖只有一个：`markitdown[all]`。脚本运行报 `ImportError` 时说明当前 Python 环境没装，现场装一次即可（全局有效，以后不再装）：

```bash
python -m pip install "markitdown[all]"
```

装了 `uv` 的机器可以不污染系统环境，改为：

```bash
uv run --with "markitdown[all]" "<skill>/scripts/convert.py" <文件路径>
```

## 输出

- 每个输入文件生成一个 `.md`，文件名沿用原文件名，**默认输出到 `~/skills`**。
- 同名文件已存在时自动加序号（`报告.md` → `报告-1.md`），不会覆盖已有结果，直接重跑是安全的。
- 脚本逐行打印 `OK 源文件 -> 输出文件`；失败的文件打印 `FAIL`/`SKIP` 到 stderr 并以非零码退出。
- 用户另外指定输出位置时，加 `--outdir <目录>`，或设环境变量 `DOC2MD_OUTDIR`。

## 转换之后

转换完成不等于任务结束。把输出文件的绝对路径告诉用户，并简要说一句转换效果——例如标题层级、表格、图片链接是否保留正常。如果结果明显有问题（内容为空、大面积乱码、PDF 是纯扫描图片提不出文字），如实告诉用户这份文件转不了或效果差，以及原因，不要把坏结果说成成功。

## 注意事项

- 拖进来的文件路径可能包含空格或中文，命令行里记得加引号。
- `.doc`（老格式）markitdown 支持有限；若失败，建议用户先另存为 `.docx`。
- 扫描版 PDF 没有文字层，转出来会是空的——这是格式限制，不是脚本故障。
