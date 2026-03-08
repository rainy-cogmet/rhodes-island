
# 🐰 罗德岛体系 - AI 协同系统

&gt; 基于 Edict 改造，以明日方舟罗德岛为原型的 AI 多 Agent 协同系统

---

## ✨ 特性

- 🎭 **11 个专业 Agent**：每个角色都有独特的人格和专业能力
- 🔄 **完整任务流转**：需求整理 → 规划拆解 → 审议把关 → 任务执行 → 质量把控
- 🛡️ **分权制衡**：模仿罗德岛的组织架构，确保任务质量和安全
- 📊 **可视化看板**：实时监控任务状态和 Agent 工作分布
- 🎨 **沉浸式体验**：完全明日方舟风格的命名和人设

---

## 🏛️ 罗德岛架构

| 角色 | Agent ID | 职责 | 原型 |
|------|----------|------|--------|
| 阿米娅 🐰 | amiya | 消息分拣、需求整理 | 罗德岛公开领袖 |
| 特蕾西娅 👑 | theresis | 规划中枢、任务拆解 | 罗德岛精神领袖 |
| 凯尔希 🩺 | kal'tsit | 审议把关、质量把控 | 罗德岛医疗总监 |
| Mon3tr 🦎 | Mon3tr | 任务调度、进度跟踪 | 凯尔希的守护者 |
| 可露希尔 🛒 | Closure | 数据处理、资源管理 | 罗德岛首席工程师 |
| 赫墨 🕊️ | Silence | 文档规范、报告撰写 | 罗德岛研究员 |
| 逻各斯 📜 | Logos | 代码开发、功能实现 | 罗德岛精英术士 |
| 塞雷娅 🛡️ | Saria | 安全审计、合规检查 | 前莱茵生命防卫科主任 |
| 德克萨斯 🗡️ | Texas | 基础设施、CI/CD | 企鹅物流员工 |
| 华法林 🌙 | warfarin | Agent管理、人事调度 | 罗德岛血库负责人 |
| 能天使 💥 | Exusiai | 每日早朝、情报聚合 | 企鹅物流员工 |

---

## 🚀 快速上手指南

### 第一步：安装 OpenClaw

罗德岛体系基于 [OpenClaw](https://openclaw.ai) 运行，请先安装：

```bash
# macOS
brew install openclaw

# 或下载安装包
# https://openclaw.ai/download
```

安装完成后初始化：

```bash
openclaw init
```

### 第二步：克隆并安装罗德岛体系

```bash
git clone https://github.com/cft0808/edict.git
cd edict
chmod +x rhodes-install.sh &amp;&amp; ./rhodes-install.sh
```

安装脚本会自动完成：
- ✅ 创建 11 个 Agent Workspace（`~/.openclaw/workspace-*`）
- ✅ 写入各角色 SOUL.md 人格文件
- ✅ 注册 Agent 及权限矩阵到 `openclaw.json`
- ✅ 配置旨意数据清洗规则
- ✅ 构建 React 前端到 `dashboard/dist/`（需 Node.js 18+）
- ✅ 初始化数据目录
- ✅ 执行首次数据同步
- ✅ 重启 Gateway 使配置生效

### 第三步：配置消息渠道

在 OpenClaw 中配置消息渠道（Feishu / Telegram / Signal），将 `amiya`（阿米娅）Agent 设为旨意入口。阿米娅会自动分拣闲聊与指令，指令类消息提炼标题后转发特蕾西娅。

```bash
# 查看当前渠道
openclaw channels list

# 添加飞书渠道（入口设为阿米娅）
openclaw channels add --type feishu --agent amiya
```

参考 OpenClaw 文档：https://docs.openclaw.ai/channels

### 第四步：启动服务

```bash
# 终端 1：数据刷新循环（每 15 秒同步）
bash scripts/run_loop.sh

# 终端 2：看板服务器
python3 dashboard/server.py

# 打开浏览器
open http://127.0.0.1:7891
```

&gt; 💡 **提示**：`run_loop.sh` 每 15 秒自动同步数据。可用 `&amp;` 后台运行。

&gt; 💡 **看板即开即用**：`server.py` 内嵌 `dashboard/dashboard.html`，无需额外构建。Docker 镜像包含预构建的 React 前端。

### 第五步：发送第一道旨意

通过消息渠道发送任务（阿米娅会自动识别并转发到特蕾西娅）：

```
请帮我用 Python 写一个文本分类器：
1. 使用 scikit-learn
2. 支持多分类
3. 输出混淆矩阵
4. 写完整的文档
```

### 第六步：观察执行过程

打开看板 http://127.0.0.1:7891

1. **📋 旨意看板** — 观察任务在各状态之间流转
2. **🔭 罗德岛调度** — 查看各部门工作分布
3. **📜 报告阁** — 任务完成后自动归档为报告

任务流转路径：
```
收件 → 阿米娅分拣 → 特蕾西娅规划 → 凯尔希审议 → 已派发 → 执行中 → 已完成
```

---

## 🎯 进阶用法

### 使用旨意模板

&gt; 看板 → 📜 旨库 → 选择模板 → 填写参数 → 下旨

9 个预设模板：周报生成 · 代码审查 · API 设计 · 竞品分析 · 数据报告 · 博客文章 · 部署方案 · 邮件文案 · 站会摘要

### 切换 Agent 模型

&gt; 看板 → ⚙️ 模型配置 → 选择新模型 → 应用更改

约 5 秒后 Gateway 自动重启生效。

### 管理技能

&gt; 看板 → 🛠️ 技能配置 → 查看已安装技能 → 点击添加新技能

### 叫停 / 取消任务

&gt; 在旨意看板或任务详情中，点击 **⏸ 叫停** 或 **🚫 取消** 按钮

### 订阅罗德岛通讯

&gt; 看板 → 📰 罗德岛通讯 → ⚙️ 订阅管理 → 选择分类 / 添加源 / 配飞书推送

---

## ❓ 故障排查

### 看板显示「服务器未启动」
```bash
# 确认服务器正在运行
python3 dashboard/server.py
```

### Agent 不响应
```bash
# 检查 Gateway 状态
openclaw gateway status

# 必要时重启
openclaw gateway restart
```

### 数据不更新
```bash
# 检查刷新循环是否运行
ps aux | grep run_loop

# 手动执行一次同步
python3 scripts/refresh_live_data.py
```

### 心跳显示红色 / 告警
```bash
# 检查对应 Agent 的进程
openclaw agent status &lt;agent-id&gt;

# 重启指定 Agent
openclaw agent restart &lt;agent-id&gt;
```

### 模型切换后不生效
等待约 5 秒让 Gateway 重启完成。仍不生效则：
```bash
python3 scripts/apply_model_changes.py
openclaw gateway restart
```

---

## 🆚 与原三省六部的区别

| 维度 | 三省六部 | 罗德岛体系 |
|-----|---------|-----------|
| 文化背景 | 中国古代官僚体系 | 明日方舟罗德岛 |
| Agent 数量 | 12 个 | 11 个 |
| 入口角色 | 太子 | 阿米娅 |
| 规划角色 | 中书省 | 特蕾西娅 |
| 把关角色 | 门下省 | 凯尔希 |
| 调度角色 | 尚书省 | Mon3tr |
| 任务ID前缀 | JJC | RHI |

---

## 📚 更多资源

- [🏠 项目首页](https://github.com/cft0808/edict)
- [📖 原版 README](README.md)
- [🤝 贡献指南](CONTRIBUTING.md)
- [💬 OpenClaw 文档](https://docs.openclaw.ai)
- [🐰 角色映射](RHODES_MAPPING.md)
- [✅ 任务清单](RHODES_TODO.md)

---

**为了感染者的未来！** 🐰✨

