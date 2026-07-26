# The Chair Reference Review

一个从招生官视角出发的留学推荐信定性诊断 Skill。

它不把推荐信当作“第三人称版本的 PS”，而是先判断招生官最关心的三件事：

1. 推荐人是否真的有资格评价申请者；
2. 评价是否有具体、可信且符合推荐人视角的证据；
3. 推荐信是否为申请者与目标项目的契合提供了独立背书，并与 CV、PS、其他推荐信形成分工。

这套方法提炼自 The 椅子的小红书帖子[《换个视角看推荐信：招生官到底想读什么？》](http://xhslink.cn/o/5FYKpmjtUPe)。

## 它会怎么工作

默认采用“两阶段”流程：

### 第一阶段：先判断

Skill 会给出：

- 一句话总判断；
- 招生官读完最可能记住的申请者形象；
- 推荐资格与观察基础；
- 证据可信度与申请者辨识度；
- 项目契合与材料组合功能；
- 每项判断的依据、影响和判断边界。

第一阶段不给默认总分，也不会直接把整封信改写掉。它会先请使用者确认、反驳或补充事实。

### 第二阶段：再建议

在使用者校准判断后，Skill 才会给出：

- 最多三个修改优先级；
- 最多五处高价值段落标注；
- 四个证据功能的保留、补证、压缩或重建建议；
- 仍需推荐人或申请者确认的事实。

## 核心方法

### 删掉形容词，还能不能看出申请者是谁？

如果删除 `outstanding`、`diligent`、`talented` 等词后，信里仍有清楚的场景、行动、结果和差异化表现，证据才真正成立。

### 细节是否符合推荐人的视角？

具体不等于越精确越好。推荐人不太可能知道的私人动机、其他实习细节或过度精确数字，会让推荐信显得像申请者代笔。Skill 会区分：

- 有合理来源的细节；
- 需要补充观察依据的信息；
- 超出推荐人视角的可信度风险。

### 推荐信是否和整套材料形成分工？

- CV 提供事实与经历结构；
- PS 解释动机、发展轨迹与项目需求；
- 推荐信提供第三方观察、比较和背书。

推荐信可以与 CV 或 PS 指向同一能力，但应增加独立证据，而不是简单复述。

## 推荐输入格式

```text
请使用 $the-chair-reference-review 对这封推荐信做定性诊断。第一轮请先判断，不给总分，也不直接重写整封信；等我确认判断后，再给修改建议。

【申请类别】
【目标学校与项目】
【项目官网或官方介绍】
【官方推荐信要求】
【字数或格式限制】

【推荐人身份】
【与申请者的关系】
【认识时间与接触频率】
【共同课程、研究、项目或工作场景】
【推荐人实际观察过的工作】

【这封信希望证明的能力】
【CV、PS 与其他推荐信的分工】
【推荐信正文或文件】
```

完整模板见 [`references/intake-template.md`](skill/the-chair-reference-review/references/intake-template.md)。

## 调用示例

```text
使用 $the-chair-reference-review 诊断这封申请 LLM 的学术推荐信。
第一轮先判断推荐资格、证据可信度和项目契合；等我确认后再给修改建议。
```

## 安装

如果你的 Skills 客户端支持从 GitHub 安装：

```bash
npx skills add zhy1126/The-Chair-Reference-Review
```

也可以下载本仓库，将：

```text
skill/the-chair-reference-review
```

复制到本地 Skills 目录，再使用：

```text
$the-chair-reference-review
```

## 仓库结构

```text
The-Chair-Reference-Review/
├─ README.md
└─ skill/
   └─ the-chair-reference-review/
      ├─ SKILL.md
      ├─ agents/
      │  └─ openai.yaml
      ├─ references/
      │  ├─ chair-principles.md
      │  ├─ diagnostic-guide.md
      │  ├─ intake-template.md
      │  └─ output-schema.md
      └─ scripts/
         └─ extract_reference_docx.py
```

## 使用边界

- 不虚构推荐关系、观察场景、排名、数字或结果；
- 不把申请者自己的反思冒充为推荐人的第一手观察；
- 不默认用数字总分替代项目和关系语境；
- 不在事实未经确认时生成整封替代信；
- 建议在分享材料前遮盖姓名、邮箱、签名、学号等个人信息。

