# 知识图谱、交互实验与题集覆盖规范

## 1. 算法知识图谱

知识图谱回答：题目属于哪里、依赖什么、展示什么机制、如何迁移。它不是标签云。

节点 ID 稳定命名空间：`domain:<slug>`、`category:<slug>`、`topic:<category>/<topic>`、`post:<slug>`、`facet:<field>:<slug>`、`path:<id>`。禁止使用标题或数组下标作为 ID。

边方向固定为 source → target：
- `belongs_to`：专题属于领域；`classified_as`：题目唯一主归属；`instantiates`：题目展示 L3 模式。
- `uses_structure`、`uses_technique`、`models`、`proved_by`：结构、技巧、问题形态、证明工具。
- `requires`：真正的先修概念；`targets_stage`：建议学习阶段。
- `includes`、`precedes_in_path`：学习路径成员与顺序。
- `extends`、`contrasts`：进阶迁移和范式对照，必须给出中文 reason。

不要把“使用哈希表”写成“必须先学完某道哈希题”。只有阅读门槛才是 requires；共享宽泛标签不构成强推荐。策划关系应显示关系类型和理由。

机器数据：`content/knowledge_graph.json`。每次新增文章/路径时同步图谱。公开 problem 节点只允许 published；节点唯一、边无悬空引用；每题恰有一个分类边和一个 L3 边；requires 与 precedes_in_path 不得形成环；路径边 position 必须与 reading_paths.json 一致。

## 2. 交互式学习实验

四级成熟度：I0 静态 SVG；I1 确定性关键帧 stepper（默认）；I2 可控参数实验（需输入范围和 oracle）；I3 可执行沙盒（需隔离、超时和规模上限）。先定义状态机，再做动画。

每个 snapshot 至少包含连续 step、operation、state、roles（active/candidate/resolved/discarded/queued/popped/evicted）、invariant、explanation；metrics 可选。UI 的图形、数值、状态表和说明必须由同一个 snapshot 驱动。关键帧摘录必须明确标注，不能伪称完整执行代码。

使用原生按钮、键盘操作、可见焦点、首尾 disabled、aria-live、prefers-reduced-motion；不自动播放；无 JS 时保留关键图解、证明和代码。浏览器测试要验证前进/后退、边界、键盘与真实语义状态变化，颜色变化不算通过。

推荐状态可视化：双指针/窗口的边界与合法性；二分的候选区间与排除理由；树图的递归栈/队列/visited；DP 的状态表与转移来源；单调栈的入栈/弹栈；LRU 的 map/list 一致性、提升和淘汰。

## 3. Blind 75 / NeetCode 150 覆盖

两套集合有重叠，分别维护，绝不能相加成 225 道独立题。入口记录在 `content/coverage.json`。题目以 problem number + canonical slug 规范化，标题不作主键。

状态语义：published（main 已发布并通过门禁）、in_progress（PR/分支）、planned（候选）、duplicate（映射既有文章）、excluded（有理由排除）、unresolved（无法匹配）。候选题不计覆盖。完整来源快照导入前 coverage_count 必须为 null，不得报告百分比。正式报告必须给出分子、分母、未决数、排除数和快照日期。

每批建议 3–5 题，先补先修闭包和模式阶梯，再扩数量。当前已进入内容建设的 P0/P1 批次包括 #242、#49、#347、#20、#206、#141、#125、#42、#424、#76；下一批候选为 #150、#21、#70、#198、#207。候选分类仍需通过至少 3 题、至少 2 个 L3 模式和独立教学边界的晋升门槛。

## 4. 每批完成定义

每批必须一起交付：官方题面核验、唯一 slug、分类与 facets、图谱关系、学习路径、至少一个高价值交互、浏览器语义测试、Python 边界/反例/差分测试、三幅原创 SVG、evidence.json、PDF 和覆盖状态。只有合并 main 后才能从 in_progress 改为 published。
