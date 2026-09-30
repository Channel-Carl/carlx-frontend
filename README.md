# CarlX Frontend

**先选风格，再制作。风格保持一致，版式与图表适应内容。**

A Chinese-first frontend design skill for AI coding agents. Compare suitable visual directions and palettes before building websites, product interfaces, dashboards, data reports, and HTML presentations.

它让 AI 先根据任务推荐 4–6 个有明确差异的风格，展示实际配色色块、用途和推荐理由；你选定方向后，再完成作品。

## 工作方式

1. 理解内容、受众、使用场景和品牌约束。
2. 推荐适合任务的风格，展示配色、字体、布局和动效气质。
3. 等待你选择、换一组或指定混搭；第一轮直接在对话中推荐。
4. 保存 `design-direction.md`，按选定体系制作完整作品。
5. 检查实际浏览器渲染、交互、数据表达与动效，再交付。

已有明确风格或设计稿时沿用；明确授权 AI 自选时直接继续。局部功能修复和沿用既有设计的增量编辑不重新启动风格选择。

## 内置内容

- **17 个风格方向、34 套角色色板**：瑞士网格、纸墨杂志、财经报刊、明亮咨询分析、研究图册、精密产品极简、暗色电影科技、暖调自然、深色雅致、机构海军蓝、强信号海报、创意几何、笔记索引、新粗野图形、印刷独立刊物、终端工程、装饰艺术几何。
- **内容驱动的版式**：网站、产品 UI、仪表盘、阅读式报告与 HTML 演示各有制作指引。
- **复杂图表支持**：组合图、双轴图、瀑布图、关系图等按分析问题选择；支持 SVG 文字、标签和图例。
- **语义动效**：按流程、数据、依赖和比较关系编排，支持减少动画与播放状态清理。
- **中文排版与渲染检查**：检查字体、长标题、密集内容、响应式布局与交互。

色板的 170 组静态不透明文本色对均通过 4.5:1 对比度检查。这不等同于实际页面的完整无障碍验收，也不代表所有风格已经完成成品实测。

## 安装

把整个仓库放入客户端支持的技能目录，目录名使用 `carlx-frontend`，保留 `references/` 和 `scripts/`。

### 使用共享技能目录

适用于已配置共享技能发现或客户端链接的环境：

```bash
git clone https://github.com/Channel-Carl/carlx-frontend.git ~/.agents/skills/carlx-frontend
```

Windows PowerShell：

```powershell
git clone https://github.com/Channel-Carl/carlx-frontend.git "$env:USERPROFILE\.agents\skills\carlx-frontend"
```

客户端已有自己的技能入口时，将入口链接到该共享目录。新安装后按客户端方式重新加载技能或开启新会话。

### 单客户端安装

也可将仓库直接克隆到客户端的用户级技能目录，例如 Claude Code 的 `~/.claude/skills/carlx-frontend` 或 Codex 的 `~/.codex/skills/carlx-frontend`。同一台机器采用共享目录时，使用链接，避免维护多份独立副本。

如果已有 `frontend-style-first` 或 `carl-frontend`，先备份并将其目录及客户端入口改为 `carlx-frontend`；避免同时启用两个相同规则的技能。

## 使用示例

支持 `$skill-name` 的客户端可显式调用：

```text
使用 $carlx-frontend 做一个科研仪器公司的官网。
面向实验室采购人员，突出产品参数、应用场景和咨询入口。
先推荐适合的风格并展示配色，等我选定后再制作。
```

```text
使用 carlx-frontend，把这份财报整理成 HTML 演示。
先推荐风格；选定后让各页版式与图表适应论证内容，加入语义动效。
```

```text
使用 carlx-frontend 做一个 SaaS 管理后台。
已有品牌蓝色，请沿用；其他视觉方向由你自行决定，直接制作。
```

这是面向 AI 的工作规则和参考库，需要支持技能加载与前端制作的 agent。它不附带固定页面模板或浏览器运行环境，也不要求安装其他前端 skill。



## 文件结构

```text
carlx-frontend/
├── SKILL.md
├── references/
│   ├── style-library.md
│   ├── design-craft.md
│   ├── content-layout-charts.md
│   ├── semantic-motion.md
│   └── consulting-presentations.md
├── scripts/
│   └── check_palettes.py
├── README.md
├── NOTICE.md
└── LICENSE
```

## 维护与校验

配色只维护在 `references/style-library.md`。修改后运行：

```bash
python scripts/check_palettes.py
```

校验脚本使用 Python 3 标准库，无第三方依赖。页面的透明层、图片、图表、焦点轮廓和交互仍需检查实际渲染。

## 来源与许可证

Copyright © 2026 Channel-Carl。采用 [GNU AGPL v3](LICENSE)（`AGPL-3.0-only`）。

风格、配色与设计方法的来源说明见 [NOTICE.md](NOTICE.md) 和各参考文件。归藏、Frontend Slides 等是参考来源，运行本技能无需安装它们。第三方品牌、字体、图片和原始报告的权利仍属于各自权利人。
