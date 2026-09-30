# 内置风格与配色库

调研及整理：2026-09-30。此处的“高级”指完整的视觉秩序、清晰的层级与适合任务的表达，不限定深色、衬线或奢华装饰。

这是一套面向前端与 HTML 演示的策展分类，部分名称为本库归纳，不能宣称都是独立的历史流派。场景建议是根据资料形成的设计判断，不是来源机构的官方适用性承诺。

## 导航与选择

| ID | 方向 | 优先场景 | 密度 | 构图辨识点 |
|---|---|---|---|---|
| swiss-grid | 瑞士网格 | 数据汇报、设计、工业科技 | 中/高 | 非对称网格、巨型数字、单色锚点 |
| editorial-paper | 纸墨杂志 | 行业观察、文化、商业叙事 | 中 | 报头、双细线、跨栏标题 |
| financial-editorial | 财经报刊 | 财报解读、研究报告、商业阅读 | 高 | 新闻层级、表格秩序、证据图版 |
| consulting-light | 明亮咨询分析 | 战略、经营、财务分析与决策演示 | 中/高 | 结论标题、开放图表、注释与比较框架 |
| research-blueprint | 研究图册 | 科研、技术报告、建筑分析 | 中/高 | 坐标、编号、图文注释 |
| product-minimal | 精密产品极简 | SaaS、后台、开发工具、文档 | 高 | 任务工作区、细边界、紧凑层级 |
| cinematic-tech | 暗色电影科技 | 技术发布、产品展示、演示舞台 | 低/中 | 主视觉舞台、暗面层次、局部光 |
| warm-organic | 暖调自然 | 可持续、生活方式、手作、建筑 | 低/中 | 材料照片、松弛留白、自然色 |
| dark-botanical | 深色雅致 | 艺术、精品品牌、文化活动 | 低 | 深底衬线、细线与少量暖色 |
| institutional-navy | 机构海军蓝 | 董事会、咨询、政策、投资人 | 中/高 | 严整证据块、克制金色与编号 |
| bold-signal | 强信号海报 | 发布会、创意机构、品牌宣言 | 低/中 | 字体作为主体、单一大色块 |
| creative-geometric | 创意几何 | 教育、创意工具、社区、工作坊 | 中 | 分色构图、几何模块、友好节奏 |
| notebook | 笔记索引 | 自学、课程、知识库、研究笔记 | 中/高 | 页签、索引、批注式结构 |
| neo-brutalist | 新粗野图形 | 独立产品、创作者、年轻品牌 | 中/高 | 硬边框、偏移阴影、拼接块 |
| retro-zine | 印刷独立刊物 | 音乐、艺术、社区、小众出版 | 中 | 胶印颗粒、窄体、纸片叠层 |
| terminal | 终端工程 | 开发者工具、CLI、技术教学 | 中/高 | 代码、命令行、等宽信息 |
| art-deco | 装饰艺术几何 | 酒店、展览、精品活动、邀请函 | 低 | 对称轴、阶梯轮廓、几何细饰 |

先按主要行为（阅读、操作、说服、体验、现场演示）、信息密度和品牌约束筛选，再看行业。科技内容也可以采用杂志体系；教育内容也不必一律粉彩。场景表不是硬路由。

从符合需求的候选中推荐 4–6 个具有明确区别的风格，每个选一套最适合任务的色板，按 SKILL.md 展示配色并等待选择，无需先制作 HTML 预览。高密度工作界面优先检查 product-minimal、research-blueprint、financial-editorial；经营/战略/财务决策演示检查 consulting-light，并按内容与其他合适方向比较；演讲或品牌展示可检查 swiss-grid、bold-signal、cinematic-tech；阅读与文化表达可检查 editorial-paper、notebook、warm-organic。不能仅按“科技=深色、环保=绿色”做推荐，也不把同一风格换色当作不同风格。

## 配色角色与证据边界

每个色板包含 bg（页底）、surface（内容底）、text（正文）、muted（辅助文字）、accent（视觉强调块）、on-accent（强调块上文字）、line（装饰分隔）。主文字与辅助文字都要在实际所在背景上可读。

accent 默认用于色块或装饰，**不自动具有链接文字、图表线或焦点色的资格**。黄色、浅粉与荧光色配深字；深色锚点配浅字。正文链接可用 text 加下划线；必要控件边界与焦点用经过对比验证的颜色，不能直接拿装饰 line 充当可识别边界。

“改编”保留来源的核心颜色，补充色彩角色并修正不适用组合；“整理设计”是本库设计的完整组合，不是某品牌的官方色板。不要声称复刻官方组件或品牌资产。实际数值在下表维护一次。

数据色与品牌色分别设计：分类、连续、发散采用相应编码，类别不能仅靠颜色区分；不能把本库强调色循环成全套图表颜色。沿用既有业务状态语义；没有既定语义时再定义，并同时提供文字/图标。投影、低亮度屏幕与打印用途需检查实际可读性。

选定方向后的执行方法见 [视觉设计规则](design-craft.md)；布局与数据问题见 [内容布局与图表](content-layout-charts.md)；动效实现见 [语义动效](semantic-motion.md)。这些规则让不同内容共享视觉体系，不把本库的构图辨识点当成固定页型。

## swiss-grid · 瑞士网格

- 适合：结构化报告、统计与路线图、设计机构、工业产品；正式度中至高。
- 边界：长篇文学阅读、大量柔和生活摄影不宜机械套网格海报。
- 语法：明确列网格与非对称对齐，标题和数字产生尺度差；内容以行、列、分区组织，不自动铺满卡片。直角、纯色与留白，网格可以隐形。
- 字体：Archivo / IBM Plex Sans；中文 Noto Sans SC。展示标题有力量，正文保持正常宽度。
- 动效：按信息顺序搭建轴线、数字与关系，短促准确；不要把每一行都飞入。
- 来源：L2/L3；历史依据 W1。以下五种是同一语法的配色变体，不算五个风格候选。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| swiss-ikb / 克莱因蓝 / L3 改编 | #FAFAF8 | #F0F0EE | #0A0A0A | #595959 | #002FA7 | #FFFFFF | #D4D4D2 |
| swiss-red / 瑞士红标 / L2 改编 | #FFFFFF | #F5F5F5 | #0A0A0A | #595959 | #FF3300 | #0A0A0A | #D4D4D4 |
| swiss-lemon / 柠檬黄 / L3 改编 | #FAFAF8 | #F0F0EE | #0A0A0A | #595959 | #FFD500 | #0A0A0A | #D4D4D2 |
| swiss-lime / 柠檬绿 / L3 改编 | #FAFAF8 | #F0F0EE | #0A0A0A | #595959 | #C5E803 | #0A0A0A | #D4D4D2 |
| swiss-orange / 工业橙 / L3 改编 | #FAFAF8 | #F0F0EE | #0A0A0A | #595959 | #FF6B35 | #0A0A0A | #D4D4D2 |

克莱因蓝不能直接用作黑底正文高亮。黄色、绿色、橙色强调块均使用深字；不要照搬原模板中橙色白字或黑底深蓝的建议。

## editorial-paper · 纸墨杂志

- 适合：行业观察、商业叙事、出版、文化、个人文章；正式度中至高。
- 边界：频繁输入、高频筛选与操作的后台不宜采用杂志式大标题和页码装饰。
- 语法：刊物识别、细线、跨栏标题、导语与引文；图表和图注成为版面的一部分。报头在封面或章节可明显，内容页可收为小型刊名/页码；主证据的面积由内容决定，不把每页做成同一双栏或同尺寸卡片。
- 字体：Playfair Display / Source Serif 4，正文可配 Work Sans；中文标题 Noto Serif SC、正文 Noto Sans SC。
- 动效：标题、细线和重点逐段组织；阅读内容静止可读，动效不改变字形宽度。
- 来源：L2 的 Paper & Ink/Vintage Editorial，L3 的墨水经典；组合均为改编。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| monocle-ink / 墨水经典 / L3 改编 | #F1EFEA | #E8E5DE | #0A0A0B | #5A5751 | #0A0A0B | #F1EFEA | #C9C4B9 |
| paper-crimson / 纸墨绯红 / L2 改编 | #FAF9F7 | #F1EEE8 | #1A1A1A | #5C5751 | #C41E3A | #FFFFFF | #D8D1C7 |
| vintage-oat / 复古燕麦 / L2 改编 | #F5F3EE | #E8D4C0 | #1A1A1A | #55504A | #8B3D2E | #FFFFFF | #D1C5B8 |

## financial-editorial · 财经报刊

- 适合：财报解读、经济分析、商业新闻、研究报告；正式度高，可承载高密度。
- 边界：品牌需要明显未来感或强视觉娱乐时，报刊基调可能过于传统。
- 语法：新闻式主次标题、数据表格秩序、图版与邻近注释、来源与单位；证据先于装饰。阅读栏适合长文，分析演示可用通栏图表、关联小多图或桥接结构；固定图表侧栏不是风格身份。重复刊头/首字下沉/背景格线按内容价值取舍，不逐页叠加。与纸墨杂志的区别是更强调密集读数与证据层级。
- 字体：Source Serif 4 + IBM Plex Sans；中文宋体标题搭无衬线图表标注。
- 动效：长期阅读区域保持稳定；演示按基线、数据变化、关键差异与结论组织播放，不能用报头入场代替证据动效。
- 来源：W2 的 FT 官方历史色板为参考；完整色板是整理设计，不称 FT 当前官方主题。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| salmon-claret / 鲑粉酒红 / W2 整理设计 | #FFF1E0 | #F6E9D8 | #26231F | #64564B | #9E2F50 | #FFFFFF | #D9CBBB |

## consulting-light · 明亮咨询分析

- 适合：战略选择、经营复盘、财务拆解、市场进入与董事会决策演示；正式度高。
- 边界：品牌故事、艺术作品和娱乐发布不必使用论证式标题；咨询方法不等于将所有网站做成办公报告。
- 语法：干净浅底、紧凑结论标题、开放的绘图区、直接数据标签与对象附近的解释。几张图需要比较时共享维度，解释变化时用桥接或分解，战略选择用带明确维度的矩阵/决策表；不同证据关系产生不同空间结构。容器只在分组有意义时使用。
- 字体：IBM Plex Sans / Arial，中文 Noto Sans SC / Microsoft YaHei；无衬线标题与图表为主要角色，数据使用等宽数字对齐。没有必须模仿的机构专用字体。
- 动效：共同框架稳定，证据按讲解阶段建立，重点差异局部聚焦，解释与结论接续；使用 [语义动效](semantic-motion.md) 的演示编排。
- 来源：W11–W13 的公开报告作为论证与图表组织样本，细节见 [咨询式论证与版面](consulting-presentations.md)。下面是本库自定的三套完整配色，不是三家机构的官方品牌色或官方 PPT 模板；三套颜色仍只算一个风格方向。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| consulting-blue / 白纸深蓝 / 整理设计 | #FFFFFF | #F2F5F8 | #162536 | #526273 | #174B78 | #FFFFFF | #D5DDE5 |
| consulting-green / 白纸松绿 / 整理设计 | #FFFFFF | #F2F6F3 | #182B24 | #516459 | #176B47 | #FFFFFF | #D4DFD8 |
| consulting-red / 白纸朱砂 / 整理设计 | #FFFFFF | #F8F3F3 | #282323 | #655858 | #B8202E | #FFFFFF | #E2D7D7 |

## research-blueprint · 研究图册

- 适合：科研成果、技术白皮书、建筑分析、研究仪器资料；正式度高。
- 边界：面向轻松消费的页面不宜塞入无意义坐标、公式或编号来装技术感。
- 语法：图版编号、坐标与尺度、细网格、对齐注释、图文证据链。图表主体有足够面积，网格轻于数据。
- 字体：IBM Plex Sans / Newsreader，标注 IBM Plex Mono / DM Mono；中文 Noto Sans SC，刊物型标题可用 Noto Serif SC。
- 动效：路径描画、实验步骤或数据关系逐层揭示；不添加不代表真实内容的扫描线。
- 来源：L3 靛蓝瓷、L4 cobalt-grid；扩展为研究界面与图册的整理语法。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| indigo-porcelain / 靛蓝瓷 / L3 改编 | #F1F3F5 | #E4E8EC | #0A1F3D | #45566D | #174B78 | #FFFFFF | #C4CDD7 |
| cobalt-ledger / 钴蓝图册 / L4 改编 | #F0EBDE | #E6E0CE | #1F2BE0 | #334077 | #1F2BE0 | #FFFFFF | #BEC1DE |

## product-minimal · 精密产品极简

- 适合：SaaS、后台、开发工具、仪表盘、文档；正式度中至高，偏操作和高密度。
- 边界：情绪和实物故事是核心的品牌页，可能需要更有表现力的视觉资产。
- 语法：工作区直接进入任务；通过字号、对齐、分隔与表面层次建立秩序。真实导航、表格、表单和状态，避免营销封面占据操作界面。
- 字体：Geist Sans / IBM Plex Sans，数据与代码 Geist Mono；中文 Noto Sans SC。字体中性是场景选择，不是品质缺陷。
- 动效：聚焦切换、任务反馈、面板过渡；不以持续背景动画制造产品感。
- 来源：W3/W4。配色为整理设计，不宣称 Geist/Linear 官方数值。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| product-white / 雾白石墨 / 整理设计 | #FAFAFA | #FFFFFF | #171717 | #666666 | #171717 | #FFFFFF | #E5E5E5 |
| product-dark / 石墨夜间 / 整理设计 | #0A0A0A | #171717 | #F5F5F5 | #A3A3A3 | #D4D4D4 | #0A0A0A | #333333 |

## cinematic-tech · 暗色电影科技

- 适合：产品发布页、技术展示、硬件/软件演示、舞台式作品集；正式度中，密度低至中。
- 边界：长时间阅读与密集表格不应靠发光、低对比灰字和玻璃层表达科技感。
- 语法：真实产品或机制主视觉占据舞台，暗面由细微色值区分，局部光服务焦点；信息区有稳定可读的实色底。
- 字体：Manrope / Satoshi；中文 Noto Sans SC。主视觉缺失时用真实机制图，不能放假产品截图。
- 动效：按产品机制编排一段揭示过程，局部光与镜头式过渡节制使用。
- 来源：L2 Neon Cyber/Electric Studio 的视觉素材归纳；界面层级参考 W4。下面是整理设计，移除双霓虹默认方案。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| midnight-ice / 午夜冰蓝 / 整理设计 | #0B1020 | #151D31 | #F4F7FC | #A6B3C8 | #80C9FF | #0B1020 | #2D3A53 |

## warm-organic · 暖调自然

- 适合：自然、可持续、生活方式、手作、材料与建筑项目；正式度中，密度低至中。
- 边界：没有自然素材依据时不要编造环保认证；深土色不能取代数据状态。
- 语法：材料或纪实照片、柔和留白、松紧有节奏的图文，少量地形/植物形状需与内容相关；圆角可有但不成为满屏胶囊。
- 字体：Fraunces / Source Serif 4 + 人文无衬线；中文 Noto Serif SC + Noto Sans SC。
- 动效：材料与图片缓慢揭示、路径或章节推进；避免所有元素漂浮。
- 来源：L3 森林墨与沙丘，L4 editorial-forest；这是前端适配后的整理语法。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| forest-ivory / 森林象牙 / L3 改编 | #F5F1E8 | #ECE7DA | #1A2E1F | #50604D | #2E4A2A | #F5F1E8 | #D0D4C5 |
| dune-earth / 沙丘陶土 / L3 改编 | #F0E6D2 | #E3D7BF | #1F1A14 | #615446 | #7C4937 | #F5F1E8 | #C9BAA0 |

## dark-botanical · 深色雅致

- 适合：艺术机构、精品品牌、文化活动、画廊；正式度中至高，密度低。
- 边界：薄衬线与小字号不适合远距离投影；不要把金色铺满或用来传达所有状态。
- 语法：深底、宽留白、衬线标题、细线和少量柔和抽象形状。实物图片有质感时让素材主导，避免廉价光斑替代。
- 字体：Cormorant / Instrument Serif + IBM Plex Sans；中文 Noto Serif SC 的可读字重。
- 动效：图像遮罩、细线伸展、重点柔和揭示；主体内容不长时间等待动画。
- 来源：L2 Dark Botanical；第二套为整理设计。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| botanical-copper / 墨黑暖铜 / L2 改编 | #0F0F0F | #1C1916 | #E8E4DF | #9A9590 | #D4A574 | #0F0F0F | #4A4037 |
| olive-champagne / 深橄榄香槟 / 整理设计 | #17211B | #233027 | #F0EADD | #B0B9AC | #D8C29D | #17211B | #47574A |

## institutional-navy · 机构海军蓝

- 适合：董事会、咨询交付、政策研究、投资人材料；正式度高，密度中至高。
- 边界：面向年轻娱乐受众可能显得距离感强；金色是视觉点缀，不是假奢华的证明。
- 语法：证据分区、编号和紧密对齐，图表与结论成组；深底用于章节或重点，可在同一体系内配浅纸内容区。
- 字体：Source Serif 4 / Cormorant + IBM Plex Sans；中文宋体标题、无衬线数据标签。
- 动效：因果关系与步骤推进，数据强调和章节转换；保持沉稳节奏。
- 来源：L4 signal/vellum。以下是根据其方向整理设计的数值，未宣称原版复刻。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| navy-gold / 海军蓝柔金 / 整理设计 | #142033 | #213148 | #F1EDE3 | #B1B9C5 | #D4B77A | #142033 | #425269 |
| navy-vellum / 深蓝羊皮纸 / 整理设计 | #162536 | #24364A | #F3E8CF | #BAC5D0 | #A7C8BE | #162536 | #485F71 |

## bold-signal · 强信号海报

- 适合：发布会、创意机构、品牌宣言、讲述者主导演示；正式度中，密度低至中。
- 边界：监管文档、密集后台、长篇阅读不宜全程大字报。
- 语法：巨大字体成为主体，单一强色块与黑白形成视觉重量，数字与标题占据明确位置；以字号和构图表达，不叠满装饰。
- 字体：Archivo Black / Barlow 900；中文 Noto Sans SC 的粗字重。英文窄体不强迫中文变窄。
- 动效：字块分段、块面切换、结论落点；重播后状态正确，不用随机旋转制造冲击。
- 来源：L2 Bold Signal，L4 studio；表现型文字关系可参照 W5，不能称为该机构官方主题。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| signal-orange / 炭黑信号橙 / L2 改编 | #1A1A1A | #2D2D2D | #FFFFFF | #BBBBBB | #FF5722 | #1A1A1A | #565656 |
| studio-acid / 黑底电黄 / L4 改编 | #1C1C1C | #242422 | #F5D200 | #D3C99A | #F5D200 | #1C1C1C | #5E5940 |

## creative-geometric · 创意几何

- 适合：教育产品、创意工具、社区、工作坊、年轻品牌；正式度低至中。
- 边界：正式政策或董事会材料不宜强行套鲜艳几何；几何装饰不承担未经说明的数据含义。
- 语法：有比例的分色面板、几何模块、友好标题与明确阅读顺序；图形需辅助分类、导航或解释。
- 字体：Syne / Plus Jakarta Sans；中文 Noto Sans SC。粗标题与正常正文形成层级。
- 动效：模块组装、形状变换、直接反馈；不能为玩形状改变关键控件位置。
- 来源：L2 Creative Voltage/Pastel Geometry/Split Pastel；表达性原则参考 W6，几何语法参考 W7。不是 Material 官方主题。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| electric-voltage / 电蓝酸黄 / L2 改编 | #1A1A2E | #24243F | #FFFFFF | #BEC4DC | #D4FF00 | #1A1A2E | #535879 |
| pastel-sage / 粉彩鼠尾草 / L2 改编 | #C8D9E6 | #FAF9F7 | #20252B | #465664 | #5A7C6A | #FFFFFF | #9AADB9 |

电蓝 #0066FF 可作为额外的大面积分色面板；放文字时单独核验，不能把深浅表面的文字色混用。粉彩只做表面，不以浅粉文字表达重点。

## notebook · 笔记索引

- 适合：自学网页、课程、知识库、研究笔记、读书材料；正式度中，可承载较高密度。
- 边界：真正需要搜索和筛选的知识库仍要实现这些功能，页签装饰不能冒充导航。
- 语法：索引、页签、批注与章节进度；知识结构决定页面，而非先画一块纸再塞内容。阅读区独立、目录可用。
- 字体：Bodoni Moda / Source Serif 4 + DM Sans；中文 Noto Serif SC 与 Noto Sans SC。
- 动效：页签切换、章节定位、批注展开；不模拟妨碍阅读的卷页。
- 来源：L2 Notebook Tabs，L3 牛皮纸。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| notebook-mint / 奶油薄荷页签 / L2 改编 | #F8F6F1 | #FFFFFF | #1A1A1A | #5C5953 | #98D4BB | #1A1A1A | #D5D1C7 |
| kraft-notes / 牛皮纸笔记 / L3 改编 | #EEDFC7 | #E0D0B6 | #2A1E13 | #5A4936 | #59422D | #F8F1E6 | #B8A78E |

## neo-brutalist · 新粗野图形

- 适合：独立产品、创作者、年轻品牌、直接有力的比较与流程；正式度低至中。
- 边界：软性精品品牌、严肃机构和精密密集工具不宜让粗边框抢走注意力。
- 语法：粗实线搭建布局、硬偏移阴影、块面相接，浅色表面配深字；结构直接而有秩序，不能把“粗野”当作可用性低的借口。
- 字体：Archivo Black / 系统无衬线粗体；中文 Noto Sans SC。
- 动效：硬切换、按压位移、模块分步出现；阴影偏移随状态有逻辑。
- 来源：L4 raw-grid 的核心配色与结构改编；不是建筑粗野主义的直接等价物。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| raw-blush / 墨线灰粉 / L4 改编 | #FFFFFF | #F2D4CF | #0A0A0A | #55504D | #E5EDD6 | #0A0A0A | #0A0A0A |

## retro-zine · 印刷独立刊物

- 适合：音乐、独立出版、文化社区、艺术作品集、小批量品牌；正式度低至中。
- 边界：纹理不能降低正文清晰度，手写与错位不能作用于严谨数字和表格。
- 语法：窄体标题、少量批注手写、纸片叠层、印刷颗粒；建立重复的纸边与分隔规则，不堆砌无关贴纸。
- 字体：Bebas Neue + Space Grotesk，手写仅用于短批注；中文 Noto Sans SC/Serif SC，避免强行压缩。
- 动效：纸片展开、印章式重点、段落节奏；微倾斜不影响读序。
- 来源：L4 retro-zine；保留其卡其底与绿色块，深绿不直接作为卡其底小字。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| zine-khaki / 卡其油墨绿 / L4 改编 | #C8B99A | #F4EFE6 | #1A1A1A | #4B473D | #008F4D | #0A0A0A | #766B56 |

## terminal · 终端工程

- 适合：CLI、开发者工具、代码教程、系统演示；正式度中，密度中至高。
- 边界：非技术消费者通常不需要终端外壳；长中文文章不宜全篇等宽。
- 语法：命令与结果明确分区、可复制代码、状态与日志可信；正文说明保留正常阅读层级，装饰游标不能假装实时运行。
- 字体：JetBrains Mono / IBM Plex Mono；中文正常无衬线，代码按实际内容选择支持字体。
- 动效：实际步骤与输出揭示，用户可跳过；没有真实运行时明确标注演示。
- 来源：L2 Terminal Green；不沿用“黑客”刻板印象作为所有科技项目默认。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| terminal-green / 终端绿 / L2 改编 | #0D1117 | #161B22 | #E6EDF3 | #9BA6B2 | #39D353 | #0D1117 | #3B4654 |

## art-deco · 装饰艺术几何

- 适合：酒店、精品活动、展览开幕、邀请函与收藏展示；正式度中至高，密度低。
- 边界：高频操作界面和密集数据不宜满屏对称装饰。Art Deco 不是单一“黑金”色系。
- 语法：对称轴、阶梯轮廓、几何线饰与精细比例，装饰与内容分区；避免把所有边框画成金线。
- 字体：Bodoni Moda / Cormorant + 克制无衬线；中文宋体展示字重，保持易读。
- 动效：轴向展开、线饰描画、章节转场；礼仪感来自节奏而非无限闪光。
- 来源：W8 的几何与装饰语言；以下为前端整理设计色板，不是历史标准色。

| 色板 ID / 名称 / 来源 | bg | surface | text | muted | accent | on-accent | line |
|---|---|---|---|---|---|---|---|
| deco-jade / 玉绿香槟 / 整理设计 | #112C28 | #1C3B35 | #F5EEDD | #BCC9BF | #D5B779 | #112C28 | #5D7768 |
| deco-ivory / 象牙深墨 / 整理设计 | #F7F0E2 | #ECE2CF | #25221D | #645A4C | #80653C | #FFFFFF | #C8B78E |

## 来源与调研依据

本库不复制完整模板或原文规范；记录来源的核心视觉要素，并用自己的语言整理适配规则。模板图像、品牌 Logo 和商业字体未作为内置资产分发。原模板的字号、舞台、库依赖与“禁止用户自定义颜色”等条款不随色板继承。

### 编写时查阅的技能资料（2026-09-30 核验）

下面的 L1–L5 是来源记录，路径描述编写时查阅的文件，不是本包内待加载的文件。完整配色与适配规则已整理在上文；使用本技能不需要这些技能或原模板。公开源仓库与署名见 [NOTICE.md](../NOTICE.md)。

- L1：`frontend-html-studio/SKILL.md` 与 `references/web-artifacts.md`、`slide-decks.md`：路由、任务优先、产品工作区、视觉选择。
- L2：`frontend-slides/STYLE_PRESETS.md`：12 个基础预设的字体、配色与构图。
- L3：`guizang-ppt-skill/references/themes.md`、`themes-swiss.md`：5 套杂志色与 4 套瑞士色。studio 对应的 `references/magazine-ppt/` 两文件与其 SHA-256 一致，视为同一来源，未重复计算。
- L4：`frontend-slides/bold-template-pack/selection-index.json`：34 个候选；读取 cobalt-grid、raw-grid、retro-zine、signal、vellum、studio、editorial-forest、soft-editorial 的 preview.md，参考其语法，不直接复制演示内容。
- L5：`impeccable/SKILL.md` 与 `reference/new-work.md`：按用户行为、受众与产品机制设计方向。没有继承其随机派发、固定提问网页或强制图像生成流程。

### 公开一手资料（2026-09-30 查阅）

- W1：[Museum für Gestaltung Zürich：Josef Müller-Brockmann](https://eshop.museum-gestaltung.ch/publikationen%40museum-gestaltung.ch?id=7726&op=product)。依据：形式简化、功能性与动态构图；本库的前端场景和色板是改编判断。
- W2：[Financial Times 官方 ui-style-guide 色板](https://github.com/Financial-Times/ui-style-guide/blob/master/index.md)。历史参考：FT Pink #FFF1E0、Tint #F6E9D8、Claret #9E2F50；不当作当前 Origami 版本承诺。当前 Origami 色彩页未能成功读取，未引用其未核验内容。
- W3：[Vercel Geist：Colors](https://vercel.com/geist/colors)。依据：背景、组件状态、边界、高对比表面与文字分角色；本库未复制其整套色阶。
- W4：[Linear：How we redesigned the Linear UI](https://linear.app/now/how-we-redesigned-the-linear-ui)。依据：减少视觉噪声、提高导航密度和层级、使用真实界面验证概念；不把产品 UI 的原则当作暗色营销页的官方定义。
- W5：[Pentagram：The Public Theater](https://www.pentagram.com/work/the-public-theater/story)。依据：活跃的文字关系与可持续身份结构；这里只作为文字构图参考。
- W6：[Google Material 3](https://m3.material.io/)。依据：表达性颜色、字体、形状与动效可结合可用性；具体 color roles 子页未能读取，本库不引用该页未核验的数值或算法。
- W7：[MoMA：Bauhaus graphic design](https://www.moma.org/explore/inside_out/2009/11/06/bauhaus-the-graphic-design-department-goes-back-to-school/)。依据：字形、网格、材料节制；不能将包豪斯简化成固定三原色加圆方三角。
- W8：[V&A：An introduction to Art Deco](https://www.vam.ac.uk/articles/an-introduction-to-art-deco)。依据：多种来源、几何与装饰语言；并非只有黑金。
- W9：[IBM Carbon：Color](https://carbondesignsystem.com/elements/color/overview/) 与 [Carbon Charts palettes](https://charts.carbondesignsystem.com/palettes)。依据：中性色组织界面，数据色按数据分组与可读性选择；没有把品牌 accent 冒充完整数据色板。
- W10：[W3C：文本对比](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)、[非文本对比](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)。校验采用普通文字 4.5:1；必要的控件/图形对比按 3:1 与实际相邻颜色检查，装饰分隔线不统一套此规则。
- W11–W13：麦肯锡 Global Banking Annual Review 2025、BCG Global Wealth Report 2025、贝恩 Global Private Equity Report 2025。官方原件链接、查阅页码与适配边界集中维护在 [咨询式论证与版面](consulting-presentations.md)；本库颜色是整理设计，静态报告不提供 HTML 动效依据。
