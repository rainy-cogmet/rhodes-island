# 罗德岛体系 - 完整修改清单

## 📋 任务状态

- [x] 第二阶段：需要修改的脚本 ✅
  - [x] scripts/sync_agent_config.py ✅
  - [x] scripts/sync_officials_stats.py ✅
  - [x] scripts/sync_from_openclaw_runtime.py ✅
  - [x] scripts/kanban_update.py ✅
  - [x] scripts/skill_manager.py ✅
  - [x] 其他 scripts/ 下的文件检查 ✅

- [ ] 第三阶段：需要修改的看板 UI
  - [ ] dashboard/dashboard.html

- [x] 第四阶段：需要创建的文档 ✅
  - [x] README_RHODES.md ✅

- [x] 第五阶段：需要检查的其他文件 ✅
  - [x] docker/demo_data/ 目录下的演示数据（发现有硬编码的三省六部内容，这是演示数据，不是必须修改的）
  - [x] docs/ 目录下的文档（发现有硬编码的三省六部内容，暂时跳过，等第三阶段一起处理）

---

## 第一阶段：已完成 ✅

### 1. 创建所有角色的 SOUL.md（11个）
- [x] agents/amiya/SOUL.md
- [x] agents/theresis/SOUL.md
- [x] agents/kaltsit/SOUL.md
- [x] agents/Mon3tr/SOUL.md
- [x] agents/Closure/SOUL.md
- [x] agents/Silence/SOUL.md
- [x] agents/Logos/SOUL.md
- [x] agents/Saria/SOUL.md
- [x] agents/Texas/SOUL.md
- [x] agents/warfarin/SOUL.md
- [x] agents/Exusiai/SOUL.md

### 2. 创建 RHODES_MAPPING.md - 角色映射文档
- [x] RHODES_MAPPING.md

### 3. 创建 rhodes-install.sh - 罗德岛安装脚本
- [x] rhodes-install.sh

---

## 第二阶段：需要修改的脚本 ✅

### 1. scripts/sync_agent_config.py ✅
- [x] 修改 ID_LABEL 字典：三省六部 → 罗德岛角色
- [x] 修改 _SOUL_DEPLOY_MAP：三省六部 → 罗德岛角色
- [x] 修改 EXTRA_AGENTS：三省六部 → 罗德岛角色
- [x] 修改 runtime_id 检查：taizi → amiya

### 2. scripts/sync_officials_stats.py ✅
- [x] 修改官员列表：三省六部 → 罗德岛角色
- [x] 修改任务ID前缀：JJC → RHI
- [x] 兼容历史：taizi → amiya

### 3. scripts/sync_from_openclaw_runtime.py ✅
- [x] 修改角色映射：三省六部 → 罗德岛角色
- [x] 修改任务ID前缀：JJC → RHI
- [x] 修改注释：军机处 → 罗德岛控制中心
- [x] 修改错误日志：JJC → RHI

### 4. scripts/kanban_update.py ✅
- [x] 修改用法示例：JJC → RHI
- [x] 修改 STATE_ORG_MAP：三省六部 → 罗德岛角色
- [x] 修改 _STATE_AGENT_MAP：三省六部 → 罗德岛角色
- [x] 修改 _ORG_AGENT_MAP：三省六部 → 罗德岛角色
- [x] 修改 _AGENT_LABELS：三省六部 → 罗德岛角色
- [x] 修改 cmd_create 中的"皇上" → "博士"
- [x] 修改 cmd_done 中的"皇上" → "博士"

### 5. scripts/skill_manager.py ✅
- [x] 修改标题注释：三省六部 → 罗德岛体系
- [x] 修改 SKILL_AGENT_MAPPING：三省六部角色 → 罗德岛角色
- [x] 修改用法示例：zhongshu/menxia/shangshu → theresis/kaltsit/Mon3tr
- [x] 修改 target_agents：menxia → kaltsit
- [x] 修改 main 函数 description：三省六部 Skill 管理工具 → 罗德岛 Skill 管理工具

### 6. 其他 scripts/ 下的文件检查 ✅
- [x] scripts/apply_model_changes.py - OK
- [x] scripts/fetch_morning_news.py - OK
- [x] scripts/file_lock.py - OK
- [x] scripts/record_demo.py - OK
- [x] scripts/refresh_live_data.py - OK
- [x] scripts/take_screenshots.py - OK
- [x] scripts/utils.py - OK

---

## 第三阶段：需要修改的看板 UI ⚠️

### 1. dashboard/dashboard.html
- [ ] 修改标题：军机处 → 罗德岛控制中心
- [ ] 修改所有硬编码的三省六部名称
- [ ] 修改任务ID前缀：JJC → RHI
- [ ] 修改配色（可选）
- [ ] 修改图标（可选）

---

## 第四阶段：需要创建的文档 ⚠️

### 1. README_RHODES.md
- [ ] 快速上手指南
- [ ] 角色介绍
- [ ] 安装说明
- [ ] 与原三省六部的区别

---

## 第五阶段：需要检查的其他文件 ⚠️

### 1. data/ 目录下的初始化文件
- [ ] 检查是否有硬编码的三省六部名称
- [ ] 检查是否有硬编码的任务ID前缀 JJC

### 2. docs/ 目录下的文档
- [ ] docs/getting-started.md（可选）
- [ ] docs/task-dispatch-architecture.md（可选）

---

## 📝 备注

- ⚠️ **重要**：修改 `agents/amiya/SOUL.md 一定要放在最后！
- ⚠️ **重要**：所有任务ID前缀从 JJC 改为 RHI（Rhodes Island）
- ⚠️ **重要**：所有角色名称从三省六部改为罗德岛角色

---

## 角色映射对照

| 三省六部 | 罗德岛角色 | Agent ID |
|---------|----------|---------|
| 太子 | 阿米娅 | amiya |
| 中书省 | 特蕾西娅 | theresis |
| 门下省 | 凯尔希 | kaltsit |
| 尚书省 | Mon3tr | Mon3tr |
| 户部 | 可露希尔 | Closure |
| 礼部 | 赫墨 | Silence |
| 兵部 | 逻各斯 | Logos |
| 刑部 | 塞雷娅 | Saria |
| 工部 | 德克萨斯 | Texas |
| 吏部 | 华法林 | warfarin |
| 早朝官 | 能天使 | Exusiai |
