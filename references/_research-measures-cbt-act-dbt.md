> ⚠️ **内部研究文件**：本文档仅为 MindMirror 项目团队的学术文献整理，**不直接用于用户对话**。内容仅供开发参考，不构成心理治疗建议或临床评估标准。如需心理健康评估，请寻求专业帮助。
>
> ---

# 心理测量与 CBT/ACT/DBT 数字化 — 学术文献检索报告

> 检索日期：2026-06-06
> 检索范围：PHQ-9/GAD-7/PSS-10 中文版信效度、数字化 CBT/ACT/DBT、LLM 认知重构、认知扭曲检测

---

## 一、心理筛查量表在中国人群中的信效度

### PHQ-9 中文版

**He, Y. 等 (2014)**
- **标题**: Reliability and validity of the Chinese version of the Patient Health Questionnaire (PHQ-9) in the general population
- **期刊**: *Comprehensive Psychiatry*
- **结论**: PHQ-9 中文版在中国一般人群中 Cronbach's α = 0.86，信效度良好。
- **项目价值**: assessment-scales.md — 提供量表信效度基础证据

**Zheng, Q. 等 (2020)**
- **标题**: Reliability and validity of the Chinese version of the Patient Health Questionnaire-9 (C-PHQ-9) in patients with psoriasis
- **期刊**: *BMJ Open*
- **结论**: 皮肤病患群体中 Cronbach's α = 0.89，因子结构稳定，支持单维结构。
- **项目价值**: assessment-scales.md — 扩展至躯体疾病共病抑郁筛查场景

### GAD-7 中文版

**Sun, J. 等 (2021)**
- **标题**: Psychometric Properties of the Generalized Anxiety Disorder Scale-7 Item (GAD-7) in a Large Sample of Chinese Adolescents
- **期刊**: *Healthcare (Basel)*
- **结论**: 67,281 名中国青少年中验证，单维结构，适用于人群水平焦虑筛查。
- **项目价值**: assessment-scales.md — 大样本青少年 GAD-7 信效度证据

**Wang 等 (2018)**
- **标题**: 广泛性焦虑量表-7在中国综合医院住院患者中的信效度研究
- **期刊**: *临床精神医学杂志*
- **结论**: 住院患者中 Cronbach's α = 0.90，最佳截断值 9 分（灵敏度 66.7%，特异度 85.8%，AUC = 0.84）。
- **项目价值**: assessment-scales.md + 量表题干翻译 — 提供中文住院患者截断值参考

**围产期人群 (2023)**
- **结论**: 围产期女性 GAD-7 AUC = 0.89，最佳截断值 ≥3.5（灵敏度 0.82）。
- **项目价值**: assessment-scales.md — 围产期特殊人群截断值调整

**心血管 ICU 患者 (2018-2019)**
- **结论**: Cronbach's α = 0.912，最佳截断值 8 分（灵敏度 90.0%，特异度 84.7%，AUC = 0.952）。
- **项目价值**: assessment-scales.md — 不同临床场景截断值差异的重要参考

### PSS-10 中文版

**Wang, Q. 等 (2024)**
- **标题**: Psychometric properties of the perceived stress scale (PSS-10) among pregnant women in China
- **期刊**: *Children and Youth Services Review*, 156
- **结论**: 双因子结构（无助感 + 自我效能感），Cronbach's α > 0.70，CFI > 0.90。
- **项目价值**: assessment-scales.md — 确认 PSS-10 中文版双因子结构

**精神分裂症家庭照护者 (2023)**
- **标题**: Psychometric validation of the Perceived Stress Scale (PSS-10) among family caregivers of people with schizophrenia in China
- **期刊**: *BMJ Open*
- **结论**: Cronbach's α = 0.79，重测信度 ICC = 0.91。
- **项目价值**: assessment-scales.md — 重测信度优异

**医学生纵向研究 (2024)**
- **标题**: Validation of the Chinese version of the Perceived Stress Scale-10 in healthcare students
- **结论**: Cronbach's α = 0.886-0.904，重测信度 ICC = 0.816，EGA 双因子结构准确率 98.65%-100%。
- **项目价值**: assessment-scales.md — 纵向测量不变性证据

**青少年 (2020/2024)**
- **结论**: 977 名中学生中验证双因子结构，支持跨性别和留守状态的测量不变性。
- **项目价值**: assessment-scales.md — 青少年人群适用性

---

## 二、数字化 CBT / ACT / DBT 工具的最新证据

### CBT 聊天机器人

**Fitzpatrick, K.K. 等 (2017)**
- **标题**: Delivering Cognitive Behavior Therapy to Young Adults With Symptoms of Depression and Anxiety Using a Fully Automated Conversational Agent (Woebot)
- **期刊**: *JMIR Mental Health*
- **结论**: 2 周内显著降低抑郁症状 (Cohen's d=0.44)，平均使用 12 次，83% 留存率。
- **项目价值**: techniques.md — CBT 聊天机器人里程碑 RCT

**Zhong, L. 等 (2024)**
- **标题**: The therapeutic effectiveness of artificial intelligence-based chatbots in alleviation of depressive and anxiety symptoms in short-course treatments
- **期刊**: *Journal of Affective Disorders*, 356, 459-469
- **结论**: 中等效应量改善。
- **项目价值**: techniques.md — 聊天机器人 CBT 荟萃分析级证据

**Li, H. 等 (2023)**
- **标题**: Systematic Review and Meta-Analysis of AI-Based Conversational Agents for Promoting Mental Health and Well-Being
- **期刊**: *NPJ Digital Medicine*, 6(1), 236
- **结论**: 全面荟萃分析证实 AI 对话代理在心理健康促进中的有效性。
- **项目价值**: techniques.md — 领域内被引用最多的综述之一

**Woebot 产后抑郁 RCT (2025)**
- **结论**: 产后抑郁 (EPDS↓5+ 分) 和焦虑 (GAD-7) 大幅改善，70%+ 达到临床显著改善，效果持续至 6 周。
- **项目价值**: techniques.md — 特定人群强证据

### ACT 数字化

**网络 ACT 系统综述 (2022)**
- **标题**: The Effects of Internet-Based Acceptance and Commitment Therapy on Process Measures
- **期刊**: *JMIR*, e39182
- **结论**: 网络 ACT 对心理灵活性等过程变量有显著改善。
- **项目价值**: techniques.md — ACT 数字化交付的过程证据

**医学生自助 ACT (2024)**
- **标题**: Effectiveness of an Internet-Based Self-Help Acceptance and Commitment Therapy Program on Medical Students' Mental Well-Being
- **期刊**: *JMIR*, e50664
- **结论**: 自助 ACT 程序对医学生心理健康有持续改善效果。
- **项目价值**: techniques.md — 自助/低强度 ACT 有效性证据

### DBT 数字化

**DBT Coach 青少年 (2020-2026)**
- **标题**: The DBT Coach App as an adjunct to a comprehensive DBT programme for adolescents
- **期刊**: *The Cognitive Behaviour Therapist*
- **结论**: 使用与 DBT 技能练习分数呈显著正相关，但临床结局改善不显著。
- **项目价值**: techniques.md — DBT 数字化辅助角色定位（技能练习增强，非替代治疗）

**DBT Coach BPD (2016)**
- **标题**: The DBT Coach mobile application as an adjunct to treatment for suicidal and self-injuring individuals with borderline personality disorder
- **期刊**: *Psychological Services* (APA)
- **结论**: 可接受性良好，可立即降低主观痛苦和自伤冲动，但使用率偏低（中位数 11.5 次）。
- **项目价值**: techniques.md — DBT 应用辅助治疗的早期证据

### 正念数字化

**Linardon, J. 等 (2024)**
- **标题**: The efficacy of mindfulness apps on symptoms of depression and anxiety: An updated meta-analysis of randomized controlled trials
- **期刊**: *Clinical Psychology Review*, 107, 102370
- **结论**: 正念应用对抑郁和焦虑症状有效。
- **项目价值**: techniques.md — 正念数字化交付的荟萃分析证据

**Wang, Y. & Farb, N. (2025)**
- **标题**: An Exploratory Study of Chatbot-Based Mindfulness for Mental Health Support
- **期刊**: *Mindfulness*, 16(11), 3143
- **结论**: 聊天机器人交付正念的可行性初步证据。
- **项目价值**: techniques.md — 聊天机器人 + 正念直接研究，与 MindMirror 技术路径高度相关

---

## 三、CBT 技术在 AI/LLM 环境中的应用

**Na, Hongbin (那洪斌) (2024)** — CBT-LLM
- **标题**: CBT-LLM: A Chinese Large Language Model for Cognitive Behavioral Therapy-based Mental Health Question Answering
- **会议**: LREC-COLING 2024, Torino, Italy
- **结论**: 首个专门面向中文 CBT 心理健康问答的大语言模型，基于 Baichuan-7B 微调。
- **项目价值**: techniques.md — **直接相关**：中文 CBT 专用 LLM 开创性工作

**Wang, Y. 等 (2025)** — CRBot
- **标题**: Evaluating an LLM-Powered Chatbot for Cognitive Restructuring: Insights from Mental Health Professionals
- **来源**: arXiv:2501.15599
- **结论**: GPT-4 驱动的 CRBot 在认知重构三阶段（探索-评估-替代）中表现良好，但存在权力不对等、"毒性积极"等风险。
- **项目价值**: techniques.md — **核心参考**：认知重构自动化的真实世界评估

**Bedi, N.S. 等 (2026)**
- **标题**: Assessing the Effectiveness of LLMs in Delivering Cognitive Behavioral Therapy
- **来源**: arXiv:2603.03862
- **结论**: LLMs 在"引导发现"上得分较高，但**在认知共情（解释性回应）上接近零分**。
- **项目价值**: techniques.md — **关键警示**：LLM 在 CBT 中的能力边界

**Sage, A. 等 (2025)**
- **标题**: A Survey of Cognitive Distortion Detection and Classification in NLP
- **会议**: EMNLP 2025 Findings, Suzhou, China
- **结论**: 首篇全面综述，涵盖 38 项研究、6 类方法，**含中文数据集 C2D2 和 SocialCD-3k**。
- **项目价值**: techniques.md — **核心技术参考**：认知扭曲自动检测完整技术地图

**AutoCBT (2025)**
- **标题**: AutoCBT: An Autonomous Multi-agent Framework for Cognitive Behavioral Therapy in Psychological Counseling
- **来源**: arXiv:2501.09426
- **结论**: 自主多智能体 CBT 框架。
- **项目价值**: techniques.md — 多智能体 CBT 系统架构参考

**LLM 心理治疗综述 (2025)**
- **标题**: A Survey of Large Language Models in Psychotherapy: Current Landscape and Future Directions
- **来源**: arXiv:2502.11095
- **结论**: 全面综述 LLM 在心理治疗中的应用现状。
- **项目价值**: techniques.md — LLM + 心理治疗全景综述

---

## 四、心理量表使用的最佳实践

**Martin-Key, N. 等 (2022)**
- **标题**: The Current State and Validity of Digital Assessment Tools for Psychiatry: Systematic Review
- **期刊**: *JMIR Mental Health*, e32824
- **结论**: 数字化心理评估工具效度良好，但**AI 聊天机器人施测量表的效度研究缺失**。
- **项目价值**: assessment-scales.md — 指出聊天机器人施测的研究空白

**UCL Discovery (2025)**
- **标题**: Validated self-administered screening tools to identify depression and anxiety
- **结论**: 自评量表数字化有效性确认，但**逐题 vs 一次性呈现的效果尚未被直接研究**。
- **项目价值**: assessment-scales.md — MindMirror 当前"逐题陪做"的做法属于探索性设计

**JMIR (2025)**
- **标题**: Generative AI Mental Health Chatbots as Therapeutic Tools
- **期刊**: *JMIR*, e78238
- **结论**: 160 个聊天机器人研究中仅 47% 测试了临床疗效，LLM 工具仅 16% 有严格测试。
- **项目价值**: assessment-scales.md + 伦理指南 — 强调证据差距和人类监督

**TherapyProbe (2026)**
- **标题**: TherapyProbe: Generating Design Knowledge for Relational Safety in Mental Health Chatbots Through Adversarial Simulation
- **来源**: arXiv:2602.22775
- **结论**: 通过对抗模拟识别心理健康聊天机器人的关系安全风险。
- **项目价值**: 伦理指南 — AI 辅助心理筛查的安全设计参考

---

## 对 MindMirror 的核心启示

| 维度 | 核心结论 | 启示 |
|------|---------|------|
| **量表信效度** | PHQ-9/GAD-7/PSS-10 中文版信效度良好，但截断值因人群而异 | 量表结果解读需注明"参考截断值" |
| **数字化 CBT** | Woebot 等有中等效应量证据 (d=0.44-0.47)，但依从性是大问题 | 设计留存机制，避免过度承诺疗效 |
| **LLM + CBT** | CBT-LLM 等专用模型出现，但共情和认知理解仍是短板 | 人机协作优于全自动 |
| **认知扭曲检测** | NLP 领域已有 38 项研究，含中文数据集 (C2D2) | 可探索集成认知扭曲识别 |
| **量表施测** | 无直接研究比较逐题 vs 一次性呈现 | "逐题陪做"属于探索性设计 |
| **伦理** | FDA 尚未批准任何 AI 心理健康设备 | 必须包含免责声明和危机转介 |

---

## 推荐优先补充的文献

1. **CBT-LLM (Na, 2024)** — 直接补充至 techniques.md
2. **Wang et al. CRBot (2025)** — 补充至 techniques.md
3. **Bedi et al. (2026)** — 补充至 techniques.md（关键警示）
4. **Sage et al. 认知扭曲检测综述 (2025)** — 补充至 techniques.md
5. **Zhong et al. 荟萃分析 (2024)** — 补充至 techniques.md
6. **Wang & Farb 聊天机器人正念 (2025)** — 补充至 techniques.md
7. **Martin-Key 数字评估工具综述 (2022)** — 补充至 assessment-scales.md
8. **Sun et al. GAD-7 青少年验证 (2021)** — 补充至 assessment-scales.md
9. **PSS-10 孕妇/照护者验证 (2023-2024)** — 补充至 assessment-scales.md
10. **JMIR 生成式 AI 聊天机器人 (2025)** — 补充至伦理指南
