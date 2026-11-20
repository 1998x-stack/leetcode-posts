# leetcode-posts

**让每一道算法题，都成为可以看见、可以证明、可以运行的推理。**

借鉴 [xm-posts](https://github.com/1998x-stack/xm-posts) 的静态出版架构和原生 SVG 可视化风格，面向大学生、研究生和算法面试学习者，用 **问题直觉 → 过程图解 → 不变量 → 复杂度 → Python 测试** 的方式理解 LeetCode 题目。

[阅读网站](https://1998x-stack.github.io/leetcode-posts/) · [算法知识地图](https://1998x-stack.github.io/leetcode-posts/topics/) · [题解归档](https://1998x-stack.github.io/leetcode-posts/archive/) · [RSS](https://1998x-stack.github.io/leetcode-posts/feed.xml) · [贡献指南](CONTRIBUTING.md)

> GitHub Pages 需要在仓库 Settings → Pages 设置为 **GitHub Actions** 来源。合并到 main 后自动构建；在 Actions 完成前不要宣称网站已部署。

## 已发布的 14 道题解

| 题目 | 专题 | 核心模式 |
|---|---|---|
| [#3 无重复字符的最长子串](posts/sliding-window/longest-substring-without-repeating-characters/index.html) | 滑动窗口 | 左边界只前进；按最后出现位置更新 |
| [#11 盛最多水的容器](posts/two-pointer/container-with-most-water/index.html) | 双指针 | 舍弃较短边的正确性证明 |
| [#15 三数之和](posts/two-pointer/three-sum/index.html) | 双指针 + 排序 | 外层去重、内层去重与固定目标 |
| [#46 全排列](posts/backtracking/permutations/index.html) | 回溯 | 选择、递归、撤销与状态恢复 |
| [#200 岛屿数量](posts/graphs/number-of-islands/index.html) | 网格图 | 连通分量、DFS、访问去重 |
| [#217 存在重复元素](posts/arrays-hashing/contains-duplicate/index.html) | 数组与哈希表 | 集合成员查询与前缀不变量 |
| [#1 两数之和](posts/arrays-hashing/two-sum/index.html) | 数组与哈希表 | 补数映射与先查后存 |
| [#238 除自身以外数组的乘积](posts/arrays-hashing/product-of-array-except-self/index.html) | 数组与哈希表 | 前后缀累计与 O(1) 辅助空间 |
| [#704 二分查找](posts/binary-search/binary-search/index.html) | 二分查找 | 闭区间与循环不变量 |
| [#34 首末位置](posts/binary-search/find-first-and-last-position/index.html) | 二分查找 | lower_bound / upper_bound |
| [#33 搜索旋转排序数组](posts/binary-search/search-in-rotated-sorted-array/index.html) | 二分查找 | 有序半区排除 |
| [#104 二叉树最大深度](posts/binary-tree/maximum-depth-of-binary-tree/index.html) | 二叉树 | 递归定义与树高 |
| [#102 二叉树层序遍历](posts/binary-tree/binary-tree-level-order-traversal/index.html) | 二叉树 | BFS 与队列分层 |
| [#543 二叉树直径](posts/binary-tree/diameter-of-binary-tree/index.html) | 二叉树 | 后序汇总与树上路径 |

每篇文章独立提供 3 幅机制相关 SVG、可键盘操作的状态演示、Python 解法和测试；题面采用原创摘要并链接官方来源。

## 基础专题学习路线

本轮已正式启用 [数组与哈希表](categories/arrays-hashing/)、[二分查找](categories/binary-search/) 和 [二叉树](categories/binary-tree/)，每个专题包含三道由浅入深的代表题。完整教学目标、先修关系和掌握标准见 [三大基础专题学习地图](docs/foundations.md)。

## 分类体系

采用 L0 学习阶段、L1 知识领域、L2 算法专题、L3 问题模式、L4 具体题目的纵向结构，并通过数据结构、技巧、问题形态、证明方法和前置知识建立横向关联。详见 [分类设计](docs/taxonomy.md)、[领域注册表](content/domains.json) 与 [横向标签词表](content/facets.json)。

## 架构

```text
content/domains.json                 # L1 知识领域与未来专题路线图
content/categories.json              # 当前启用的 L2 专题与 L3 问题模式
content/facets.json                  # 横向知识关系的受控词表
content/posts.json                   # 发布清单、唯一主归属与多维 facets
content/reading_paths.json           # 专题学习路径
posts/<category>/<slug>/index.html   # 图解文章
posts/<category>/<slug>/assets/*.svg # 自绘机制图
posts/<category>/<slug>/solution.py  # 可运行 Python 解法
posts/<category>/<slug>/evidence.json# 题源、正确性与复杂度证据
skills/olah-style-leetcode-posts/    # 权威 Skill
scripts/build_site.py                # 首页、分类、归档、搜索、RSS、站点地图
scripts/render_pdfs.py               # 增量预渲染 PDF
.github/workflows/publish.yml       # 验证及 GitHub Pages 部署
```

## 本地构建和验证

```bash
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
python scripts/sync_skills.py --check
python scripts/build_site.py
python scripts/validate_site.py
python -m pytest -q
python scripts/browser_check_all.py
```

本地预览：`cd _site && python -m http.server 8000`。生成的 `_site/` 和 `.pdf-cache/` 不要提交。生产默认路径为 `/leetcode-posts/`。

## 更新规范

阅读 [AGENTS.md](AGENTS.md)、[Skill](skills/olah-style-leetcode-posts/SKILL.md) 和 [分类规则](docs/taxonomy.md)。发布前必须核对官方题目难度和约束；编写不变量证明、反例和复杂度；构建、校验与浏览器检查完成后再将条目标记为 published。发布后的每篇文章有独特封面、相关推荐与稳定链接。
