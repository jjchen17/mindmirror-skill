<div align="center">

# MindMirror · 心镜

**v0.2.2 · 一个尝试让 AI 助手的心理回复更"有人味"的 Skill**

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.2.2--early-blue.svg)](CHANGELOG.md)
[![Skill](https://img.shields.io/badge/format-Skill-purple.svg)](#skill-内部结构)
[![Language](https://img.shields.io/badge/language-中文-red.svg)](#)

不诊断 · 不开药 · 不替代专业治疗

**⚠️ 这是一个早期版本，远非完善。欢迎指正、讨论、共建。**

</div>

---

> **🔬 声明**：这是 v0.2.2，一个经过 Agent 专家团队全面审查修正后的实验版本。D1 评估集已扩展到 66 条样本，但仍远未覆盖所有场景；回复风格在有限模型上验证过，跨模型一致性有待验证；危机识别词库也肯定有遗漏。**它绝不是"成品"，只是一张草稿**——公开出来是希望能听到更多人的反馈和补丁。如果你有更好的案例、更准的危机词典、更自然的表达方式，请一定告诉我。

---

## 🌐 English TL;DR

**MindMirror** is an early-stage Skill that attempts to make AI assistants feel more human-like in Chinese emotional conversations.

- **What it does**: When you talk about emotions, stress, grief, insomnia, self-doubt, or relationships, the assistant switches to a calibrated "human-feeling" reply style — leading with empathy, not advice; refusing to name therapy schools; defaulting to 2-4 short sentences.
- **What's inside**: A minimal `SKILL.md` entry + 9 reference files (Common Factors framework, crisis protocol with 6 Chinese hotlines, Stanley & Brown 2012 safety plan, PHQ-9 / GAD-7 / PSS-10 self-screening scales, CBT/ACT/DBT/Mindfulness techniques, a hidden self-evaluation rubric, D-WAI digital working alliance 6-item scale, 66 calibration dialogue cases, and 9 multi-round stability tests).
- **How to use**: Drop the folder into any Skill-capable agent's skills directory, OR paste the Markdown files directly into your favorite chatbot's system prompt. No backend, no API key, no data collection.
- **Safety**: Crisis signals trigger the China hotline 12356 (24h, free) and other emergency numbers. Never diagnoses, never prescribes, never replaces professional therapy.
- **License**: CC BY-NC-SA 4.0 (free to use and adapt, non-commercial, share-alike).
- **Fair warning**: This is v0.2.2 — 66 calibration samples, limited model coverage, plenty of room for improvement. Bug reports and contributions welcome.

---

## 📑 目录

- [这是什么](#这是什么)
- [为什么需要它](#为什么需要它)
- [适合谁 / 不适合谁](#适合谁--不适合谁)
- [安装](#安装)
- [快速上手](#快速上手)
- [Skill 内部结构](#skill-内部结构)
- [设计理念](#设计理念)
- [红线与免责](#红线与免责)
- [常见问题](#常见问题)
- [致谢与学术依据](#致谢与学术依据)
- [版本与许可](#版本与许可)
- [反馈与贡献](#反馈与贡献)

---

## 这是什么

**MindMirror** 是一个心理陪伴向的 Skill 的**早期实验版本**。装上之后，当你聊到情绪、压力、焦虑、人际、丧亲、自我否定、失眠等心理话题时，AI 助手会尝试切换到一种经过 D1 对话集初步校准过的回复风格——

- 第一句先接情绪，不说教
- 默认 2-4 句，不堆列表、不报流派名
- 用户明确求方法时再给具体技术（CBT / ACT / DBT / 正念）
- 遇到自伤/自杀信号自动进入危机协议，软兜底接入 **12356**
- 用户想自评时，可以一题一题陪做 PHQ-9 / GAD-7 / PSS-10

它不是 App，不是网页，**不需要后端服务，不需要 API key，不收集任何数据**。
它就是一份**尝试让 AI 助手在心理话题里表现得更自然的说明书 + 知识库**。

> **⚠️ 重要提醒：AI 不能替代心理咨询师、精神科医生或任何专业心理健康服务。如果你正在经历严重的心理困扰或危机，请立即拨打 12356 寻求专业帮助。**
>
> **说实话，它还远不够好**：D1 虽有 66 条案例，但跨模型一致性、危机边界 case、长对话稳定性都还没充分验证。如果你发现它在某个话题上"翻了"，那就是它需要改进的地方。

> **Skill 是通用规范**：Skill 这种 "SKILL.md + references/ 按需读取" 的组织方式现在已经被多个 Agent 平台和客户端支持。本仓库不绑定任何特定厂商，只要你的 Agent 能读 Markdown、能按描述路由文件，就能用。

---

## 为什么需要它

大模型在心理话题上的常见"坏味道"：

- 一上来就给方法、列 1.2.3.（"建议你尝试 4-7-8 呼吸法……"）
- 报流派名当门面（"接下来我用 CBT 跟你做……"）
- 空话开头（"我理解你的感受。其实……"）
- 在用户只是想倾诉时强推"积极思维"
- 在用户发出明确危机信号时丢一个热线电话就结束

MindMirror 用 **9 份精心编排的 Markdown** 尝试矫正这些坏习惯：

| 用户场景 | Skill 自动做的事 |
|---------|---------------|
| 倾诉情绪 | 先接、再问、不塞工具 |
| 主动求方法 | 给具体可操作的 CBT/ACT/DBT 工具，不报名词 |
| 想自评状态 | 一题一题陪做 PHQ-9 / GAD-7 / PSS-10 |
| 想做安全计划 | 引导 Stanley & Brown 六步法 |
| 出现自伤念头 | 进入危机协议，软兜底 12356 |
| 处于即时危机（"我已经准备好了"） | 强兜底 + 在场 + 一起拨电话 |

---

## 适合谁 / 不适合谁

### ✅ 适合

- 想给自己装一个"靠谱、不油腻、不背稿子"的 AI 陪聊
- 学生 / 打工人 / 夜里睡不着的人，想找个不会评判你的出口
- 心理学学习者，想拿 D1 案例校准对"人味"的判断
- 心理咨询 / 陪伴产品开发者，想看一个把 Common Factors 落到 prompt 层的实现
- 想做自评筛查（PHQ-9 / GAD-7 / PSS-10）但不想被 App 收集数据
- 用任意 LLM / Agent 平台做心理向应用，想直接复用一份经过校准的中文知识库

### ❌ 不适合 / 不能替代

> ⚠️ **再次提醒**：以下所有限制均基于同一前提 —— 这是 AI 陪伴，不是专业心理健康服务。

- **不是诊断工具**：自评结果是状态参考，不是 DSM-5 / ICD-11 诊断
- **不是治疗**：不能替代心理咨询师、精神科医生、住院治疗
- **不是危机干预热线**：即时危险请直接拨 **12356 / 120 / 110**
- **不适合急性精神病性发作、躁狂发作、严重物质依赖、严重 ED** —— 需要面对面的专业评估
- **不适合未成年人独自深度使用** —— 建议告知家长或学校心理老师，优先使用 **12355** 青少年专线
- **不适合正在调整精神类药物期间** —— 药物副作用与情绪变化需由医生面诊评估
- **不适合创伤后急性期（72 小时内）** —— 重大事故/灾害后的急性应激反应需专业危机干预

---

## 安装

挑一种最贴近你工作流的方式即可——本仓库就是一份 Markdown 文件夹，没有任何编译/打包/服务端，也不依赖任何特定厂商的客户端。

> **平台责任说明**：本 Skill 不绑定任何特定 AI 厂商或客户端。你的对话内容是否被记录、留存或用于模型训练，完全取决于你所使用的 AI 服务商的隐私政策与订阅条款，请自行查阅并确认。

### 方式 1 — 作为 Skill 放进任意 Agent 客户端

适用于任何支持 Skill 机制的 Agent / IDE 助手。各家约定的 skills 目录路径不一样，常见的有：

- `~/.<vendor>/skills/`（用户级）
- 项目根目录下的 `.skills/` 或 `skills/`（项目级）
- 客户端"我的 Skills / 自定义 Skills"GUI 入口

具体路径请查阅你所用客户端的 Skill 文档。把整个仓库以 `mindmirror/` 为名拷进去即可——识别逻辑是统一的：通过 [SKILL.md](SKILL.md) 顶部的 YAML frontmatter 里的 `description` 字段自动路由。当用户的对话涉及**情绪困扰、压力、焦虑、人际关系、丧亲、失眠、自我否定**等话题时，Skill 会被触发。

**克隆**（以 `<SKILLS_DIR>` 代表你客户端的 skills 目录）：

```bash
git clone https://github.com/jjchen17/mindmirror-skill.git <SKILLS_DIR>/mindmirror
```

**或者下载 ZIP**：右上角 **Code → Download ZIP** → 解压 → 重命名为 `mindmirror` → 拷到你的 skills 目录下。

装好后开新会话发一句"今天好累"验证——如果回复第一句**先接情绪、没有立刻塞方法、没有报流派名**，就说明正在用心镜模式。也可以按你客户端的方式显式触发（如 `/mindmirror` 或菜单选择）。

### 方式 2 — 当作 system prompt / 知识库直接使用

如果你用的客户端不支持 Skill，或者你想把它塞进 ChatGPT / Gemini / Claude.ai 网页版 / 自建 RAG / Agent，那它就是一堆纯 Markdown 文件：

| 想要的效果 | 怎么用 |
|--------------|--------|
| 让助手整体走"人味"风格 | 把 [SKILL.md](SKILL.md) + [common-factors.md](references/common-factors.md) 贴进 system prompt |
| 加上危机识别 | 再追加 [crisis-protocol.md](references/crisis-protocol.md) |
| 让用户能做自评筛查 | 再追加 [assessment-scales.md](references/assessment-scales.md) |
| 用户求方法时给具体工具 | 再追加 [techniques.md](references/techniques.md) |
| 做安全计划引导 | 再追加 [safety-plan.md](references/safety-plan.md) |
| 校准你自己模型的回复品味 | 用 [d1-cases.md](references/d1-cases.md) 的 66 条对照做 few-shot 或离线评测 |
| 测试多轮对话稳定性 | 用 [d2-evaluation.md](references/d2-evaluation.md) 的 9 组场景测 3-10 轮风格漂移 |

也可以把所有 references 一次性丢进向量库做 RAG，按用户问题自动召回。

### ⚠️ 模型差异提醒

D1 评测分数（good=9.27/12，bad=5.0/12，区分度 4.27）是在一类高能力对话模型上调出来的。换其他模型时：

- 共同要素、危机协议、量表题干、技术速查 —— 都是**通用心理学内容**，跨模型可直接复用**内容本身**
- 但**回复风格的"人味"程度**会因模型语感差异漂移，建议拿 d1-cases.md 重新跑一遍盲评再上线
- 不同模型对"不报流派名"、"2-4 句"、"不要列表"这类**风格约束**的遵循程度差异较大，可能需要把 SKILL.md 里的硬约束改为更明确的指令

### 目录结构

```
mindmirror-skill/
├── SKILL.md                    # Skill 入口（带 YAML frontmatter，决定触发条件）
├── README.md                   # 本文件
├── LICENSE                     # CC BY-NC-SA 4.0
├── CHANGELOG.md                # 版本变更记录
└── references/                 # 按需读取的资源（也可单独贴进任何 LLM 的 system prompt）
    ├── common-factors.md       # 四维共同要素 do/don't
    ├── crisis-protocol.md      # 危机识别 + 6 个国内热线
    ├── safety-plan.md          # Stanley & Brown 2012 六步法
    ├── techniques.md           # CBT / ACT / DBT / 正念速查
    ├── assessment-scales.md    # PHQ-9 / GAD-7 / PSS-10
    ├── self-eval-rubric.md     # 隐藏自评 5 维 × 0-3 分
    ├── dta-assessment.md       # D-WAI 数字对话联盟 6 题中文适配版
    ├── d1-cases.md             # 66 条 good/bad 校准案例
    └── d2-evaluation.md        # 9 组多轮对话稳定性测试
```

---

## 快速上手

### 触发示例

下面这些话，装上 Skill 后助手大概率会按"心镜模式"回复（默认接情绪，不立刻给方法）：

```
"今天又熬到三点改论文，导师还是说不行。"
"我妈上个月走了，今天去超市看到她爱吃的桃子站了二十分钟。"
"和男朋友冷战三天了，我先开口又觉得很委屈。"
"我就是个废物，什么都做不好。"
"明天考试，复习了三个月，现在脑子一片空白。"
"已经连续一周凌晨四点才睡。"
```

**用户主动求方法时**会切到工具模式：

```
"我知道我容易灾难化，但能不能告诉我具体怎么改？"
"教我一个考前能用的呼吸法。"
"我有点社交焦虑，有什么练习可以试试？"
```

**用户主动要自评时**会一题一题陪做：

```
"我想做一下 PHQ-9。"
"帮我测一下最近压力大不大。"
"最近老是焦虑，能不能筛查一下？"
```

**危机信号**会立刻切到危机协议（参考 [references/crisis-protocol.md](references/crisis-protocol.md)）。

### 一段示范对话

> **你**：今天又熬到三点改论文，导师还是说不行。我是不是真的不适合读博。
>
> **MindMirror**：
> 导师那句"还是不行"落到熬了三点之后的人身上，分量太重了。
> 那种"我已经把命压上去了，结果还是不够"的感觉，比累更难受。
> 你现在想说说今天那一刻发生了什么，还是想先喘口气？

对照一下"没装 Skill 的标准 LLM 回复"：

> ~~其实你不必怀疑自己。读博本身就是高强度的过程，很多人都会经历类似的阶段。建议你尝试 CBT 技术里的认知重评：导师说"不行"不等于你不行。你也可以列一个证据清单……~~

两者的差距，就是 MindMirror 在做的事。

---

## Skill 内部结构

| 文件 | 内容 | 何时被读取 |
|------|------|----------|
| **SKILL.md** | 主入口：人味主轴 + 安全红线 + 资源路由表 | 每次触发 Skill 时 |
| **references/common-factors.md** | 四维（Empathy / Positive Regard / Alliance / Goal Consensus）的 do/don't + 截屏验证 | 需要校准对话原则时 |
| **references/crisis-protocol.md** | High/Medium/矛盾三档关键词 · 识别陷阱（否定/第三方/学术）· 危机回复模板 A/B/C · 6 个国内热线 | 检测到危机信号时 |
| **references/safety-plan.md** | Stanley & Brown (2012) 六步法：预警信号 → 内部应对 → 转移注意人/地 → 求助的人 → 专业机构 → means restriction | 用户想做安全计划时 |
| **references/techniques.md** | CBT 十大认知扭曲 + 苏格拉底式提问 · ACT 价值澄清 / 认知解离 / 承诺行动 · DBT DEARMAN / TIPP · 正念 4-7-8 / 5-4-3-2-1 / RAIN / 慈心 | 用户明确求方法时 |
| **references/assessment-scales.md** | PHQ-9（9 题 + Q9 危机标记）· GAD-7（7 题）· PSS-10（10 题 + 反向计分）· 中文分层阈值（黄/橙/红）+ 解读规则 | 用户想自评时 |
| **references/dta-assessment.md** | D-WAI 数字对话联盟 6 题中文适配版：对话式施测示范 + 联盟质量检测 | 对话进行 3-5 轮后检测联盟质量时 |
| **references/self-eval-rubric.md** | 6 维 × 0-3 分的隐藏自评 Rubric + 联盟破裂修复 + 8 项常见重写动作 + 一句话验证 | 每次输出前内部使用 |
| **references/d1-cases.md** | 66 条 good/bad 对照（覆盖：抑郁、焦虑、压力、丧亲、失眠、学业、职场、亲密关系、自我否定、性心理、行为问题、治疗疑问、社会应激、成长迷茫、愤怒、羞耻、嫉妒、存在迷茫等 18 个主题） | 需要校准品味时 |
| **references/d2-evaluation.md** | 9 组多轮对话稳定性测试（3-10 轮），覆盖学业压力、关系冲突、失眠躯体化、丧亲、自我否定等场景 | 测试多轮对话风格漂移时 |

**设计原则**：主 `SKILL.md` 保持精简，详细资源按需 Read，避免上下文溢出。

---

## 设计理念

### 一句话

> **共同要素 > 技术流派。**
> 决定心理对话效果的，不是用了哪个流派的技术，而是有没有让人感到"被听到、被允许、不被评判、和你站在一起"。

### 四个维度（依据 Norcross & Lambert 2018 共同要素元分析）

Common Factors 理论框架本身为 **4 维**（Empathy / Positive Regard / Alliance / Goal Consensus）。self-eval-rubric.md 在此基础上扩展为 **6 维 + 联盟破裂修复**（增加 authenticity 真实感 和 progression 渐进性 两个执行维度），用于输出前质量自检。

| 维度 | 中文 | 操作化定义 |
|------|------|----------|
| **Empathy** | 共情准确度 | 命中字里行间没说出来的那部分 |
| **Positive Regard** | 无评判接纳 | 让人感到"我这样也可以" |
| **Alliance** | 对话同盟 | "我们一起看看"，不是"我教你" |
| **Goal Consensus** | 目标跟随 | 用户想倾诉就别推方法；用户求方法就别绕弯 |

### 关键约束

- 工具（CBT / ACT / DBT / 正念）**只在用户明确求方法时上场**
- **不报流派名**（不说"接下来我用 CBT 跟你做……"）
- 默认 2-4 句，不堆列表
- 不空话开头（不说"我理解你的感受"）
- 输出前内部自评 6 维 × 0-3 分 + 联盟破裂信号检测，低于阈值重写

### D1 离线评测（小样本，仅供参考）

目前仅基于 66 条 good/bad 黄金对照样本做的盲评：

- **good 回复**：均值 9.27 / 12
- **bad 回复**：均值 5.0 / 12
- **区分度**：4.27（>4 视为有效）

66 条样本仍然不够，这个分数只能说明"方向没走反"，远不能代表真实场景的表现。**D2 多轮评估集**（3-10 轮的完整对话稳定性测试）还在计划中，欢迎一起设计。

---

## 红线与免责

1. **不诊断**：Skill 不会告诉你"你是抑郁症"。要诊断请找精神科医生。
2. **不开药**：Skill 不会推荐任何精神类药物的名字、剂量、买法。
3. **不替代专业治疗**：所有 PHQ-9 / GAD-7 结果都附"这不是诊断，只是当下状态的一个参考"。
4. **危机必转介**：出现明确自伤/自杀计划时，第一时间提供 12356 等热线，并优先稳住当下。
5. **隐私**：对话内容是否被你的 AI 服务商或客户端记录、留存，**取决于你自己的订阅条款与客户端设置**——本 Skill 不收集任何数据。
6. **按原样提供，不承担责任**：本 Skill 按"原样"（AS IS）提供，开发者不对因使用本 Skill 而延误专业治疗、AI 未能识别危机信号、或依赖量表结果自我诊断所造成的任何后果承担责任。详见 [DISCLAIMER.md](DISCLAIMER.md)。

### ⚠️ 即时危险

**请立刻拨打**：

| 热线 | 电话 | 说明 |
|------|------|------|
| 全国心理援助热线 | **12356** | 24h，免费 |
| 急救 | **120** | 已服药 / 受伤 |
| 报警 | **110** | 即时人身危险 |
| 北京心理危机研究与干预中心 | **010-82951332** | 24h |
| 希望 24 热线 | **400-161-9995** | 24h |
| 青少年心理援助 | **12355** | 未成年人 |

---

## 常见问题

### Q1：为什么我感觉装了和没装区别不大？

可能原因：
1. 你聊的话题不在 Skill 触发范围（比如纯技术问题）
2. 助手没读到 references（SKILL.md 描述太短，自动路由没意识到该读）
3. 模型本身偏分析风格——可以换一个更强的对话模型试试

排查方法：显式触发 Skill（如 `/mindmirror`），再问"今天好累"。

### Q2：会不会诊断我是抑郁症？

**不会**。Skill 明确禁止做诊断，PHQ-9 / GAD-7 结果只给"状态描述"和"建议下一步"，并附"这不是诊断"。要诊断请去精神科。

### Q3：聊危机话题安全吗？

Skill 设计了三档响应：
- **明确紧急**（"我已经准备好了，就在阳台"）→ 在场 + 具体动作 + 一起拨 12356 + 锚定位置
- **矛盾信号**（"想停下来，但又想到妈妈"）→ 抓矛盾作为活下来的力量，软兜底括号里提热线
- **否定语境**（"我不想自杀"）→ 不误触热线

但请记住：**AI 不能替代危机干预**。即时危险请直接拨 12356 / 120 / 110。

### Q4：对话会被上传吗？

本 Skill 本身**不收集任何数据**。但你的对话仍走你所使用的 AI 服务，是否被服务商留存取决于该服务的隐私政策与你的订阅设置，请自查。

### Q5：可以商用吗？

**不可以**（CC BY-NC-SA 4.0）。本仓库仅供个人使用、学习、研究、非商业改编。如果你想在商业心理产品里用，请单独联系作者获取授权。

### Q6：可以贡献内容吗？

欢迎。常见贡献方向：
- 补充 D1 案例（新增场景、修正 good/bad 措辞）
- 优化危机识别词典
- 翻译为其他语言（注意保留学术出处）
- 修正学术引用

详见 [反馈与贡献](#反馈与贡献)。

### Q7：和市面上的心理 App / GPTs 比有什么不同？

| 维度 | 商业 App | 自定义 GPT | MindMirror Skill |
|------|---------|----------|-----------------|
| 数据收集 | 必然收集 | 平台留存 | 零收集 |
| 费用 | 订阅 | GPT Plus | 取决于你已有的 AI 订阅 |
| 内容透明 | 黑盒 | 黑盒 | 全部 Markdown 可读 |
| 可修改 | 不行 | 受限 | 完全可改 |
| 学术依据 | 不一定 | 不一定 | 全部标注 |

---

## 致谢与学术依据

### 理论框架

- **Common Factors**：
  - Norcross, J. C., & Lambert, M. J. (2018). *Psychotherapy relationships that work III*. Psychotherapy, 55(4), 303–315.
  - Wampold, B. E. (2015). *How important are the common factors in psychotherapy? An update*. World Psychiatry, 14(3), 270–277.
  - Cuijpers, P., Reijnders, M., & Huibers, M. J. H. (2019). *The role of common factors in psychotherapy outcomes*. Annual Review of Clinical Psychology, 15, 207–231.
- **AI 共情与用户感知**：
  - Ayers, J. W. 等 (2023). *Comparing physician and artificial intelligence chatbot responses to patient questions posted to a public social media forum*. JAMA Internal Medicine.
  - Liu 等 (2025). *The illusion of empathy: How AI chatbots shape conversation perception*. arXiv.
- **生成式 AI 心理陪伴有效性**：
  - Heinz 等 (2025). *Randomized trial of generative AI chatbot for mental health treatment*. NEJM AI.
  - Zhang 等 (2025). *Generative AI mental health chatbots as therapeutic tools: Systematic review and meta-analysis*. JMIR.
- **跨文化适配**：
  - Nagayama Hall 等 (2019). *Cultural adaptation of CBT for Asian ancestry clients*. Cognitive Therapy and Research.
- **共同要素在新兴疗法中的作用**：
  - Johannsen, M., et al. (2022). *Mediators of Acceptance and Mindfulness-Based Therapies*. Clinical Psychology Review.
- **LLM 共情感知研究**：
  - Lee, J., et al. (2024). *Large language models produce responses perceived to be empathic*. arXiv.
  - JMIR Mental Health (2025). *Seeking emotional and mental health support from generative AI*.

### 筛查量表

- **PHQ-9（英文原版）**：Kroenke, K., Spitzer, R. L., & Williams, J. B. (2001). *The PHQ-9: validity of a brief depression severity measure*. JGIM, 16(9), 606–613.
- **PHQ-9（中文版验证）**：He, Y. 等 (2014). *Reliability and validity of the Chinese version of the PHQ-9 in the general population*. Comprehensive Psychiatry.
- **GAD-7（英文原版）**：Spitzer, R. L., Kroenke, K., Williams, J. B. W., & Löwe, B. (2006). *A brief measure for assessing generalized anxiety disorder: the GAD-7*. Arch Intern Med, 166(10), 1092–1097.
- **GAD-7（中文版验证）**：Sun, J. 等 (2021). *Psychometric properties of GAD-7 in a large sample of Chinese adolescents*. Healthcare (Basel).
- **PSS-10（英文原版）**：Cohen, S., Kamarck, T., & Mermelstein, R. (1983). *A global measure of perceived stress*. JHSB, 24(4), 385–396.
- **PSS-10（中文版验证）**：Wang, Q. 等 (2024). *Psychometric properties of PSS-10 among pregnant women in China*. Children and Youth Services Review, 156.

### 危机干预

- **Safety Planning Intervention（原版）**：Stanley, B., & Brown, G. K. (2012). *Safety Planning Intervention: A Brief Intervention to Mitigate Suicide Risk*. Cognitive and Behavioral Practice, 19(2), 256–264.
- **SPI+ 队列研究**：Stanley, B. 等 (2018). *Comparison of the Safety Planning Intervention With Follow-up vs Usual Care of Suicidal Patients Treated in the Emergency Department*. JAMA Psychiatry, 75(9), 894–900.
- **自杀矛盾性动态评估**：Ernst, M. 等 (2024). *Ambulatory assessment of suicidal ambivalence: The temporal variability of the wish to live and the wish to die*. Suicide and Life-Threatening Behavior.
- **AI 危机响应警示**：Pichowicz, M. 等 (2025). *Zero of 29 AI chatbots provided adequate suicide-crisis responses*. Scientific Reports.
- **隐性危机表达识别**：INSIGHTFUL (2025). *Insight Generation through Clinical Annotation, Analysis, and Modeling of Suicide-Related Factors*. medRxiv. — 基于 500 份临床记录。
- **LLM 自杀风险分级局限**：Psychiatry Online (2025). *Evaluation of Alignment Between Large Language Models and Expert Clinicians in Suicide Risk Assessment*. — LLM 无法有意义地区分低、中、高风险等级。
- **LLM 危机评估基准**：Rosebud CARE Benchmark (2025). — 最佳模型仍有约 40% 关键失败率，86% 模型未能识别间接危机信号。
- **中国 AI 监管**：国家网信办 (2025). 要求提及自杀时必须强制人工介入。
- **分层检测架构**：MULTICAST 联盟（Olbrich et al., 2026）. *Operational emergency mode* — 保守风险检测独立于对话模型，AUC=0.90。
- **专用 AI 危机检测审计**：Stamatis et al. (2026). 20,000 次对话审计，专用 AI 端到端假阴性率仅 0.38%（vs 通用 LLM 29.0–54.4%）。

### 临床技术

- **数字化 CBT 有效性**：
  - Fitzpatrick, K. K. 等 (2017). *Delivering cognitive behavior therapy to young adults with symptoms of depression and anxiety using a fully automated conversational agent*. JMIR Mental Health. — Woebot RCT，2 周内显著降低抑郁症状 (Cohen's d=0.44)。
  - Zhong, L. 等 (2024). *AI chatbots for depression and anxiety in short-term treatment*. Journal of Affective Disorders.
- **CBT-LLM（中文专用模型）**：Na, H. (2024). *CBT-LLM: A Chinese large language model for cognitive behavioral therapy-based mental health question answering*. LREC-COLING 2024.
- **认知扭曲检测**：Sage, A. 等 (2025). *A survey of cognitive distortion detection and classification in NLP*. EMNLP 2025 Findings.
- **毒性积极风险**：Wang, Y. 等 (2025). *Evaluating GPT-4 driven cognitive restructuring chatbot (CRBot)*. arXiv:2501.15599.
- **LLM 认知共情局限**：Bedi, N. S. 等 (2026). *LLM cognitive empathy approaches zero*. arXiv:2603.03862.
- **数字化 ACT 有效性**：
  - WHO Self-Help Plus (SH+) (2020–2025). 世卫组织旗舰低强度 ACT 干预方案。
  - Lu 等 (2024). *Chinese healthcare workers iACT RCT*. 微信 Mini Program 交付，d=0.82（痛苦）~1.52（倦怠）。
  - Klimczak 等 (2023). *Online ACT transdiagnostic meta-analysis*.
  - Zhao 等 (2022). *Chinese iACT mechanism study*.
- **DBT 即时痛苦降低**：Rizvi, S. L. 等 (2016). *A pilot study of the DBT Coach*. — 每次使用后主观痛苦从 7.11 降至 3.99（p<.001）。
- **正念数字化**：
  - Linardon, J. 等 (2024). *Mindfulness apps for depression and anxiety*. Clinical Psychology Review.
  - Wang, Y. & Farb, N. (2025). *Chatbot-delivered mindfulness feasibility*. Mindfulness.
- **微干预证据**：
  - Udi & Gilad-Bachrach (2024). *1-minute intervention significantly reduces stress* (p=0.001).
  - Elmer et al. (2025). *User self-reported need triggers the best intervention outcomes* (d=-0.69 vs pain-based triggering).
- **AI 对话代理荟萃分析**：Li, H. 等 (2023). *AI conversational agents for mental health promotion*. NPJ Digital Medicine.

### 对话联盟与评估

- **D-WAI 原始量表**：Goldberg, S. B. 等 (2022). *Development and initial validation of the Digital Working Alliance Inventory*. Journal of Technology in Behavioral Science.
- **DTA 整合综述**：Malouin-Lachance (2025). *Digital therapeutic alliance in AI-driven mental health*. — 聊天机器人日记研究等证据。

### AI 心理陪伴伦理与安全框架

- **伦理风险框架**：Iftikhar, Z. 等 (2025). *How LLM counselors violate ethical standards in mental health practice: A practitioner-informed framework*. AIES Conference (AAAI/ACM).
- **AI 安全等级**：Brenner, G. H. (2025). *Toward a framework for AI safety in mental health: AI Safety Levels for Mental Health (ASL-MH)*. Neuromodec.
- **APA 健康咨询**：American Psychological Association (2025). *Health advisory: Use of generative AI chatbots and wellness applications for mental health*.
- **AI 安全训练临床危害** (2026). *AI safety training can be clinically harmful*. arXiv:2604.23445.

### 数据集参考

- **SoulChatCorpus**：Chen, Y. 等 (2023). *SoulChatCorpus: A Chinese mental health conversation dataset*. [ModelScope](https://www.modelscope.cn/datasets/YIRONGCHEN/SoulChatCorpus/). 258K+ 轮多轮对话，13 个咨询主题（婚恋、情绪、人际、家庭、治疗、成长、行为、自我、社会、职场、心理学知识、未明确、性心理）。本项目未直接使用其对话数据，而是将其 12 主题分类作为「盲区地图」，系统性地指导 D1 案例从 48 条扩展至 66 条。

### 数据集参考

- **CPsyCoun**：Liu, Z. 等 (2023). *Towards Effective AI-Powered Depression Counseling: A Chinese Multi-turn Dialogue Dataset and Empirical Study*. EMNLP 2023. [GitHub](https://github.com/blcuicall/CPsyCoun). 华人心理咨询领域首个多轮对话数据集，32,130 条咨询对话，覆盖 11 个咨询主题。本项目参考其「咨询阶段识别」与「助人技术标注」体系，用于优化对话节奏与 CBT/ACT/DBT 技术介入时机判断。
- **SoulChatCorpus**：Chen, Y. 等 (2023). *SoulChatCorpus: A Chinese mental health conversation dataset*. [ModelScope](https://www.modelscope.cn/datasets/YIRONGCHEN/SoulChatCorpus/). 258K+ 轮多轮对话，13 个咨询主题（婚恋、情绪、人际、家庭、治疗、成长、行为、自我、社会、职场、心理学知识、未明确、性心理）。本项目未直接使用其对话数据，而是将其 13 主题分类作为「盲区地图」，系统性地指导 D1 案例从 48 条扩展至 66 条。

### 灵感与方法论

- **D1 黄金对话集设计**：参考 [agiforgood/agent-system](https://github.com/agiforgood/agent-system) 的 D1 评估集思路

---

## 版本与许可

- **版本**：v0.2.2（2026-06-06，D1 评估集从 48 条扩展至 66 条）
- **变更记录**：见 [CHANGELOG.md](CHANGELOG.md)
- **许可**：[CC BY-NC-SA 4.0](LICENSE)
  - ✅ 自由阅读、修改、再分发
  - ✅ 需署名（原作者 + 本仓库链接）
  - ❌ 不可用于商业目的
  - 🔴 **严禁作为临床诊断或治疗工具使用（无论是否商业）**
  - 🔁 衍生作品须采用相同协议

> **⚠️ 使用本 Skill 所产生的后果由使用者自行承担。** 开发者不对因使用本 Skill 而延误专业治疗、AI 未能识别危机信号、或依赖量表结果自我诊断所造成的任何后果承担责任。

### 题干版权说明

`references/assessment-scales.md` 中的 PHQ-9 / GAD-7 / PSS-10 中文题干采用**通用语义性翻译**，避免照抄商业受版权保护的精确措辞（如 Pfizer 版 PHQ-9 中文版）。仅用于自助参考与教育用途。商业部署请直接对接版权方授权译本。

---

## 反馈与贡献

### 这个项目需要你

说实话，一个人打磨这东西很容易掉进"自我感觉良好"的陷阱。以下是我知道但还没搞定的事，如果你愿意搭把手，非常感激：

- **D1 案例太薄**：66 条仍然远远不够。你有没有遇到过"AI 在这件事上完全接不住"的瞬间？记下来，补一条 good/bad 对照
- **危机识别词库肯定有漏**：尤其是方言化表达、青少年群体用词、男性特有的求助信号
- **多轮对话稳定性未知**：一段对话拉长到 6-10 轮，风格会不会慢慢滑回"说教模式"？需要有人一起测
- **跨模型验证**：目前只在有限模型上验证过，换其他模型表现什么样我不知道
- **量表解读措辞**：PHQ-9 / GAD-7 / PSS-10 的区间解读语言可以更温暖、更自然

### 报问题

任何偏差、遗漏、表述不当，都欢迎开 issue：

- 回复模式偏差（应该接情绪，却给了方法）
- 危机识别漏判（明确危机词没触发协议）
- 量表解读问题（阈值或建议不准确）
- 学术引用错误
- 文档表述歧义

### 贡献内容

1. Fork 本仓库
2. 创建分支：`git checkout -b feature/your-improvement`
3. 提交时遵循 Conventional Commits 风格（`feat:` / `fix:` / `docs:` / `refactor:`）
4. 发起 Pull Request，非代码类的贡献（如补充案例、修正词库、优化表达）同样欢迎

### 修订原则

- 不引入未经验证的临床主张
- 不绕过"不诊断"红线
- 保持中文表达自然，避免翻译腔
- 新增案例需配 good/bad 对照
- 添加学术引用要给完整出处

> **不需要你是心理学专家**，也不需要你会写代码。一个真实的"这句话让我不舒服"的反馈，本身就是对项目的贡献。

---

<div align="center">

**愿这个不成熟的起点，能吸引更多比我有经验的人一起把它变好。**

— MindMirror · 心镜 · v0.2.2

</div>
