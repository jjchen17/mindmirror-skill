# 变更记录

本项目采用 [语义化版本](https://semver.org/lang/zh-CN/) 规范。
格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

## [Unreleased]

### 计划中

- 补充 D2 评估集（更复杂的多轮对话校准样本）
- 提供英文版 references（i18n）
- 增加更多文化适配（港澳台用词、海外华人场景）

---

## [0.1.0] — 2026-06-06

### 首发

**项目定位**：把 Claude 调成"有人味的心理陪伴者"的 Claude Code Skill。

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
- **references/d1-cases.md**：15 条 good/bad 校准案例

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
