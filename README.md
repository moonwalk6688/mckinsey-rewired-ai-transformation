# 《Rewired》第二版：Codex 学习技能

这是一个可在 Codex 中调用的独立学习技能，包含 39 章笔记、术语表、方法库、速查表和来源质量说明。技能名：`mckinsey-rewired-ai-transformation`。

## 安装到另一台电脑

```bash
git clone https://github.com/moonwalk6688/mckinsey-rewired-ai-transformation.git
cd mckinsey-rewired-ai-transformation
py install.py
```

上面是 Windows 命令；macOS/Linux 使用 `python3 install.py`。

安装脚本默认复制到 `~/.codex/skills/mckinsey-rewired-ai-transformation`，不会覆盖已有目录。也可指定位置：

```bash
py install.py --skills-dir /path/to/.codex/skills
```

重新开启 Codex 对话后，输入 `$mckinsey-rewired-ai-transformation` 并提问。例如：`$mckinsey-rewired-ai-transformation 从第一章开始教我，并在每章结束时测验我。`

也可以使用 Codex 的 `skill-installer` 从本仓库的 `skills/mckinsey-rewired-ai-transformation` 安装。

## 内容与来源

- [技能入口](skills/mckinsey-rewired-ai-transformation/SKILL.md)
- [章节目录](skills/mckinsey-rewired-ai-transformation/chapters)
- [方法库](skills/mckinsey-rewired-ai-transformation/patterns.md)与[速查表](skills/mckinsey-rewired-ai-transformation/cheatsheet.md)
- [来源质量说明](skills/mckinsey-rewired-ai-transformation/references/source-quality.md)

本仓库只发布独立整理的学习笔记和工具，不包含原书 PDF、完整 OCR 文本或图片。原著版权归原作者及出版方。笔记基于用户提供的 OCR 可见文字；图表、公式及识别有误的段落应回原书核对。

`scripts/read_source.py` 仅供持有对应本地 OCR 文件的读者核对原句和行号。例如：

```bash
py skills/mckinsey-rewired-ai-transformation/scripts/read_source.py --source /path/to/your-book.md --chapter 1 --limit 20
```

脚本会校验源文件 SHA-256；其他版本的行号可能不同。没有相同 OCR 文件时，仍可正常使用技能中的章节笔记。
