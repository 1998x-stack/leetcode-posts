# AGENTS.md — leetcode-posts

适用于所有编辑、文章、技能、CI 和部署变更。算法正确性与可复现性优先于视觉效果。

## 目标和来源
- 面向大学生、研究生和面试学习者，解释 **为什么算法正确**，不止提供通过样例的代码。
- 分类体系：`content/domains.json`（L1 领域与路线图）、`content/categories.json`（当前 L2 专题与 L3 模式）、`content/facets.json`（横向受控标签）；文章状态、唯一主归属、facets、封面和原题链接：`content/posts.json`。
- 每篇已发布文章只能有一个 `category` + `topic` 主归属；多维知识关联写入 `facets`，不得复制文章或用自由标签替代受控 facets。
- 文章源码: `posts/<category>/<slug>/index.html`；独立 SVG: 同目录 `assets/*.svg`；证据: `evidence.json`；Python 参考实现: `solution.py`。
- 站点生成: `scripts/build_site.py`；GitHub Pages: `.github/workflows/publish.yml`；不要提交 `_site/`。
- Skill 正本: `skills/olah-style-leetcode-posts/`；必须同步 `.claude/`、`.pi/`、`.agent/`、`.opencode/` 的镜像。

## 解题文章质量门禁
1. **题目事实**：核对 LeetCode 编号、官方难度、输入输出、关键约束；不得整段复制受版权保护的题面，用原创中文复述并链接原题。
2. **循序渐进**：用真实样例手推朴素思路，再解释优化、状态定义和循环不变量；给反例与边界条件。
3. **复杂度与证明**：讲清时间和空间复杂度计算所依赖的假设；不能将递归栈、结果集、排序额外空间略去。
4. **SVG**：每篇至少三幅与算法机制相关的独立原创 SVG，专属封面、不同状态与错误示范，不得统一占位。提供 viewBox、title、可读文字和准确图注。
5. **可交互**：用可键盘操作的逐步执行演示。页面无 JS 时应仍能阅读正确的静态图解。
6. **代码**：Python 标准库实现、可运行单测；包含空输入、重复项与题目允许的边界，不报告未执行的测试为通过。
7. **可用性**：每篇一个 H1、语义化 section/figure、响应式/打印/减少动画支持；检查手机 360/390px、桌面和页面溢出。
8. **出版**：仅 `status: published` 出现在首页、归档、搜索、RSS；封面来自文章自身 SVG，封面说明独特；PR 验证，合并 main 后部署 Pages，再检查线上 URL。

## 分类与知识关联
- 新题先阅读 `docs/taxonomy.md`；优先使用已有 L2/L3，只有满足专题晋升条件时才新增分类。
- 每篇已发布文章必须填写 `facets.structures`、`techniques`、`problem_shapes`、`reasoning`、`prerequisites` 和 `learning_stage`，所有值必须来自 `content/facets.json`。
- `content/domains.json` 中的规划方向不等于已启用分类；不要为规划方向创建空文章或伪造发布数量。

## 新增题解
```bash
python scripts/new_post.py sliding-window example-problem --topic variable-window --title '题目标题' --subtitle '一句话目标' --problem-url https://leetcode.com/problems/example-problem/
python scripts/sync_skills.py --check
python scripts/build_site.py
python scripts/validate_site.py
python -m pytest -q
```

不要只复制经典题解代码。**必须**说明「不变量 → 指针/递归转移 → 何时结束 → 为什么不漏/不重」。
