# 变更记录

本项目采用 [语义化版本](https://semver.org/lang/zh-CN/) 规范。
格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

## [Unreleased]

### 计划中

- 补充 D2 评估集（更复杂的多轮对话校准样本）
- 提供英文版 references（i18n）
- 增加更多文化适配（港澳台用词、海外华人场景）

---

## [0.2.0] — 2026-06-06

### 基于 200+ 次学术搜索的系统性优化

本轮优化基于 `D:\DESK\玩AI\Kimi_Agent_学术论文检索` 中 10 个维度 + 12 条跨维度洞察的系统性文献综述（300+ 篇文献），由 5 个并行 Agent 专家分别负责 Common Factors、量表、危机协议、技术工具库、中文文化适配五个模块。

### 新增

- **SKILL.md**：
  - 新增"文化躯体化窗口"触发策略（从睡眠/食欲/疲劳等躯体症状切入对话）
  - 新增"用户-技术匹配时机判断"分层响应地图（4 层：被听到 → 陪伴探索 → 工具介入 → 调整匹配）
  - 回复风格细化为"第 1-2 轮允许 4-6 句（联盟关键窗口），第 3 轮起恢复 2-4 句"

- **references/common-factors.md**：
  - 共情章节新增"认知共情句式模板"（"你是因为[情境]才感到[情绪]，还叠加了[深层因素]"）
  - 积极关注章节新增"反评判性语言禁忌清单"（机械模板、敷衍中立、过早视角转换）
  - 新增"理解 → 接纳 → 温和挑战"三段式回复模式（应对 GPT-4o 谄媚效应）
  - 新增"联盟破裂信号监测"（简短回应、怀疑表达、沉默 → 修复话术）

- **references/crisis-protocol.md**：
  - 新增"分层检测架构"（L1 关键词匹配 / L2 语义分析 / L3 上下文评估）
  - 危机词库扩展：躯体化危机信号（胸口闷、浑身疼、失眠数月等）、网络隐语（累了毁灭吧、想休息了等）
  - 矛盾信号扩展：经济/责任型牵挂（房贷、照顾者角色）

- **references/assessment-scales.md**：
  - PHQ-9/GAD-7 引入中文分层阈值（PHQ-9: ≥7 黄色 / ≥10 橙色 / ≥15 红色；GAD-7: ≥6 黄色 / ≥10 橙色 / ≥15 红色），附学术依据
  - 危机触发条件细化为分层矩阵（红色危机 / 黄色关注 / PSS-10 复合触发）
  - 新增"温和反馈三段式"话术模板（描述性等级 + 正常化陈述 + 个性化资源）
  - PHQ-9 第 3/5/8 项增加文化敏感澄清示例
  - PSS-10 新增双维度结果呈现（无助感维度 + 自我效能感维度），附解读示例

- **references/techniques.md**：
  - CBT 苏格拉底提问升级为"递进式认知重估对话链"（5 步：识别自动化思维 → 质疑证据 → 生成替代解释 → 评估效用 → 记录强化）
  - DBT TIPP 升级为"场景化分步引导"（含 STOP 前置、分步指令、0-10 分即时评估）
  - ACT 新增"用户匹配依据"（经验性回避识别 + 匹配决策树）
  - 新增"微干预时长参考"表（CBT 2-3min / DBT 1-2min / ACT 3-5min 等）
  - 新增"5 分钟规则"（降低回避与拖延的有效策略）

- **references/safety-plan.md**：
  - 新增"结构化随访序列"（SPI+ 证据应用：第 1/3/7/14/30/60 天 + 每月 Caring Contacts）
  - 新增"青少年用户特殊响应路径"（Caring Contacts 短信优先、12355 优先、家庭参与引导）
  - 新增"面子保护原则"（不用标签化表述、强调匿名、肯定求助行为）

- **references/self-eval-rubric.md**：
  - 新增"联盟破裂信号"过程性自检维度（rupture_repair 0-3 分）

### 学术依据更新

新增引用 30+ 篇核心文献，涵盖：
- PHQ-9/GAD-7 中文截断值研究（Wang 2014; Liu 2016; Chen 2010; Manea 2012 IPDMA 元分析; Tong 2016; Cochrane 2025）
- PSS-10 双因子结构（Lu 2017; Huang 2020; Kogar 2024 元分析）
- 认知共情 vs 情感共情差距（Liu 2025; CHI 2026 元分析）
- DBT Coach 即时痛苦降低（Rizvi 2016）
- 中国 iACT 大效应量（Lu 2024; Zhao 2022）
- SPI+ 随访 45% 风险降低（Stanley 2018）
- 分层检测架构（MULTICAST 2026; Stamatis 2026）
- 微干预证据（Udi 2024; Elmer 2025; D-MIST 框架）
- 面子机制与华人心理健康（中科院 2023; SSRPH/SSOSH 研究）

---

## [0.1.0] — 2026-06-06

### 首发

**项目定位**：把 AI 助手调成"有人味的心理陪伴者"的 Skill。

### 新增

- **SKILL.md**：主入口，含 YAML frontmatter（决定触发条件）
- **README.md**：完整项目说明（中文主体 + 英文 TL;DR）
- **LICENSE**：CC BY-NC-SA 4.0
- **references/common-factors.md**：四维共同要素 do/don't（依据 Norcross & Lambert 2018）
- **references/crisis-protocol.md**：High/Medium/矛盾三档关键词识别、危机回复模板 A/B/C、6 个国内热线
- **references/safety-plan.md**：Stanley & Brown (2012) 六步法
- **references/techniques.md**：CBT 十大认知扭曲 + 苏格拉底式提问 / ACT 价值澄清 / DBT DEARMAN + TIPP / 正念 4-7-8 + 5-4-3-2-1 + RAIN + 慈心
- **references/assessment-scales.md**：PHQ-9（含 Q9 危机标记）、GAD-7、PSS-10（含反向计分公式）完整题目 + 阈值 + 解读
- **references/self-eval-rubric.md**：输出前隐藏自评 4 维 × 0-3 分 + 8 项常见重写动作
- **references/d1-cases.md**：20 条 good/bad 校准案例

### 安全设计

- 矛盾自伤念头识别（D1-009 类型）：抓"想停 vs 想到亲人"作为活下来的力量，软兜底
- 紧急危机响应（D1-010 类型）：在场 → 具体动作（means restriction）→ 一起拨电话 → 锚定位置
- 否定语境识别（"我不想自杀"）：不误触热线
- AI 出口自检：不诊断、不开药、不替代专业

### 评测

D1 离线评测分布：
- good 回复均值：9.27 / 12
- bad 回复均值：5.0 / 12
- 区分度：4.27（有效）

### 学术依据

完整列在 README 的"致谢与学术依据"节，涵盖：
- Common Factors 元分析（Norcross & Lambert 2018; Wampold 2015）
- PHQ-9（Kroenke 2001）/ GAD-7（Spitzer 2006）/ PSS-10（Cohen 1983）
- Safety Planning（Stanley & Brown 2012）
- CBT / ACT / DBT / 正念标准教材体系
- D1 方法论灵感来自 agiforgood/agent-system

### 已知限制

- Skill 由 Claude 自主路由 references，可能在某些上下文下未触发完整资源加载
- 中文情感表达受限于 base model 语感天花板，不同 Claude 版本表现可能不同
- 题干采用通用语义性翻译，商业部署需对接版权方授权译本（如 Pfizer 版 PHQ-9）

[Unreleased]: https://github.com/jjchen17/mindmirror-skill/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/jjchen17/mindmirror-skill/releases/tag/v0.1.0
