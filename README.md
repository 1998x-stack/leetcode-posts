# leetcode-posts

**让每一道算法题，都成为可以看见、可以证明、可以运行的推理。**

借鉴 [xm-posts](https://github.com/1998x-stack/xm-posts) 的静态出版架构和 SVG 可视化风格，面向大学生、研究生和算法面试学习者，用 **问题直觉 → 状态不变量 → 正确性证明 → Python 测试** 建立可迁移的算法理解。

[阅读网站](https://1998x-stack.github.io/leetcode-posts/) · [算法知识地图](https://1998x-stack.github.io/leetcode-posts/topics/) · [题解归档](https://1998x-stack.github.io/leetcode-posts/archive/) · [RSS](https://1998x-stack.github.io/leetcode-posts/feed.xml) · [贡献指南](CONTRIBUTING.md)

## 已发布：10 道 Medium

| 题目 | 专题 | 核心模式 |
|---|---|---|
| [#3 无重复字符的最长子串](posts/sliding-window/longest-substring-without-repeating-characters/index.html) | 滑动窗口 | 左边界单调前进 |
| [#11 盛最多水的容器](posts/two-pointer/container-with-most-water/index.html) | 双指针 | 舍弃较短边的证明 |
| [#15 三数之和](posts/two-pointer/three-sum/index.html) | 双指针 | 排序、去重与候选收缩 |
| [#46 全排列](posts/backtracking/permutations/index.html) | 回溯 | 选择、递归、撤销 |
| [#200 岛屿数量](posts/graphs/number-of-islands/index.html) | 图与网格 | 连通分量与 DFS |
| [#33 搜索旋转排序数组](posts/binary-search/search-in-rotated-sorted-array/index.html) | 二分查找 | 识别有序半区 |
| [#322 零钱兑换](posts/dynamic-programming/coin-change/index.html) | 动态规划 | 完全背包与最优子结构 |
| [#739 每日温度](posts/monotonic-stack/daily-temperatures/index.html) | 单调栈 | 下一个更大元素 |
| [#102 二叉树的层序遍历](posts/trees/binary-tree-level-order-traversal/index.html) | 树与遍历 | FIFO 队列与层级边界 |
| [#146 LRU 缓存](posts/data-structures/lru-cache/index.html) | 数据结构设计 | 哈希表 + 双向链表 |

每篇文章包含三幅独立 SVG、可交互执行轨迹、算法不变量、正确性证明、复杂度拆解、Python 实现和测试。题面使用原创摘要并链接官方来源。

## Skill v2

权威 Skill 位于 [skills/olah-style-leetcode-posts](skills/olah-style-leetcode-posts/SKILL.md)，并同步至 Claude、Pi、Agent、OpenCode。v2 增加模式识别与证明模板、差分测试、复杂度审计、SVG 分镜、交互可访问性和发布门禁。

## Architecture

```text
content/categories.json              # 分类与二级专题
content/posts.json                   # 发布清单，draft 不输出
content/reading_paths.json           # 编辑策划的学习路径
posts/<category>/<slug>/index.html   # 图解文章
posts/<category>/<slug>/assets/*.svg # 独立原创图
posts/<category>/<slug>/solution.py  # Python 参考实现
posts/<category>/<slug>/evidence.json# 来源、证明和复杂度证据
skills/olah-style-leetcode-posts/    # Skill v2 正本
scripts/build_site.py                # 首页、分类、归档、搜索、RSS、站点地图
scripts/render_pdfs.py               # 增量预渲染 PDF
.github/workflows/publish.yml       # 验证与 GitHub Pages 部署
```

## Local build and QA

```bash
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
python scripts/sync_skills.py --check
python -m pytest -q
python scripts/audit_svg.py
python scripts/build_site.py
python scripts/validate_site.py
python scripts/browser_check_all.py --workers 2
python scripts/render_pdfs.py
python scripts/validate_site.py --require-pdfs
```

本地预览：`cd _site && python -m http.server 8000`。不要提交 `_site/` 或 `.pdf-cache/`。

## Editorial policy

阅读 [AGENTS.md](AGENTS.md)、[Skill v2](skills/olah-style-leetcode-posts/SKILL.md)、[分类规范](docs/taxonomy.md) 和 [题解规范](docs/editorial.md)。新文章先核验官方题目，再写 problem brief、证明、测试和三幅 SVG。只有所有门禁通过后才标记为 published。
