# AGENTS.md — leetcode-posts

本文件是所有代理、自动化任务和贡献者的强制工作约定。算法正确性、知识关系准确性、可访问性和可复现性优先于文章数量与视觉效果。

## 1. 权威数据源

- `content/domains.json`：L1 领域与规划路线；规划不等于已启用。
- `content/categories.json`：当前 L2 专题与 L3 模式。
- `content/facets.json`：受控横向概念词表。
- `content/posts.json`：文章状态、唯一主归属、facets、封面和原题 URL。
- `content/reading_paths.json`：有目标和理由的学习顺序。
- `content/knowledge_graph.json`：类型化节点和有方向的知识关系。
- `content/coverage.json`：Blind 75 / NeetCode 150 覆盖状态和候选队列。
- `skills/olah-style-leetcode-posts/`：唯一 Skill 正本。
- `AGENTS.md`：仓库级执行规范。

已发布 URL `posts/<category>/<slug>/` 是稳定接口。改分类时保持 slug/URL；迁移必须提供兼容策略。

## 2. 内容与分类

- 面向大学生、研究生和面试学习者。按“题意 → 朴素思路 → 优化动机 → 状态 → 不变量/递推 → 证明 → 代码 → 复杂度”展开。
- 每篇只有一个 `category` + `topic` 主归属。辅助机制进入 facets 和知识图谱。
- 新 L2 晋升至少有 3 道可规划题、2 个有教学价值的 L3 模式、清晰边界、独立证明机制和连续学习路线；否则使用现有专题或 facets。
- published 文章必须填写 structures、techniques、problem_shapes、reasoning、prerequisites 和 learning_stage，值全部来自受控词表。
- prerequisite 表示真实阅读门槛，不等于文章“用到了”的工具。

## 3. 知识图谱协议

遵循 `docs/learning-system.md`。节点 ID：`domain:<slug>`、`category:<slug>`、`topic:<category>/<topic>`、`post:<slug>`、`facet:<field>:<slug>`、`path:<id>`。边方向为 source → target。

允许边：`belongs_to`、`classified_as`、`instantiates`、`uses_structure`、`uses_technique`、`models`、`proved_by`、`requires`、`targets_stage`、`includes`、`precedes_in_path`、`extends`、`contrasts`。requires 与 precedes_in_path 表示教学依赖/顺序，必须无环。策划的 extends/contrasts 必须写中文 reason。共享标签不自动成为推荐或先修关系。

每次新增/改分类/改路径时更新图谱。自动检查唯一 ID、悬空引用、边类型、published 状态、每题唯一主归属和路径顺序。

## 4. 交互式学习协议

遵循 `docs/learning-system.md`：I0 静态图、I1 确定性 stepper（默认）、I2 有界参数实验（需 oracle）、I3 隔离执行沙盒（需超时/资源限制）。先设计状态机；snapshot 至少有 step、operation、state、roles、invariant、explanation。所有图形、数字、指标和说明由同一 snapshot 驱动。关键帧摘录要明确标注，不能假称完整执行。

使用原生按钮、键盘操作、可见焦点、首尾 disabled、aria-live、prefers-reduced-motion；不自动播放；无 JS 保留关键内容。测试前进/后退、边界、键盘和真实状态变化，颜色变化不算通过。

## 5. 题集覆盖协议

Blind 75 与 NeetCode 150 分别管理且高度重叠，禁止相加。以 problem number + canonical slug 匹配。状态：published、in_progress、planned、duplicate、excluded、unresolved。完整 dated source snapshot 导入前 coverage_count 必须为 null，不报告百分比。正式报告给出分子、分母、未决、排除和快照日期。候选题不算覆盖。

每批 3–5 题，优先补先修闭包和模式阶梯。每批同步文章、图谱、路线、交互、测试、coverage 和 Skill 镜像。

## 6. 文章质量门禁

1. 核对官方题号、标题、难度、接口、约束和输入语义；原创复述题意。
2. 手推小例子与朴素解法，解释优化前提、状态、不变量、终止和证明。
3. 区分时间、辅助空间、递归栈、输出空间、哈希期望复杂度、排序和输入修改。
4. 至少三幅独立 SVG：机制封面、真实状态轨迹、反例/边界。
5. Python 标准库解法可运行，覆盖边界、反例和可行的差分/穷举测试。
6. 交互状态与代码/证明/SVG一致；无 JS 仍可学习。
7. 检查 360/390/768/1440px、溢出、焦点、键盘、控制台、链接、打印和减少动画。
8. 未执行的测试或未完成的浏览器检查不得报告为通过。

## 7. Skill 与发布流程

唯一编辑位置：`skills/olah-style-leetcode-posts/`。执行 `python scripts/sync_skills.py` 和 `python scripts/sync_skills.py --check`，保证 .claude/.pi/.agent/.opencode 四套镜像逐文件一致。

标准门禁：
```bash
python scripts/sync_skills.py --check
python -m pytest -q
python scripts/audit_svg.py
python scripts/build_site.py
python scripts/validate_site.py
python scripts/browser_check_all.py --workers 2
python scripts/render_pdfs.py
python scripts/validate_site.py --require-pdfs
```

新内容走 feature branch + PR。合并不等于部署；等待 Pages deploy 成功并核验公开 URL。

## 8. 完成定义

内容正确、分类合理、facets 注册、图谱边有效、路径有理由、交互可访问可测试、覆盖状态准确、Skill 镜像同步、CI 全通过、Pages 独立核验，缺一不可。
