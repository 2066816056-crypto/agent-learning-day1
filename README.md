\# 我的第一个 AI Agent 学习仓库



这个仓库包含我学习 AI Agent 开发时的两个入门示例。



\## 项目一：基础对话测试（test\_agent.py）

\- 功能：调用 DeepSeek API，完成一次简单的对话。

\- 运行方法：设置 `DEEPSEEK\_API\_KEY` 环境变量后，运行 `python test\_agent.py`。



\## 项目二：计算器 Agent（calculator\_agent.py）

\- 功能：利用 Function Calling 实现一个能调用计算器工具的 Agent。

\- 核心技术：工具调用循环、messages 管理。

\- 运行方法：设置 `DEEPSEEK\_API\_KEY` 环境变量后，运行 `python calculator\_agent.py`。



\## 如何设置 API Key（安全方式）

1\. 在 PowerShell 中执行：

&#x20;  ```powershell

&#x20;  $env:DEEPSEEK\_API\_KEY="你的真实key"

