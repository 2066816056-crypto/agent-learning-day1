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



计算器agent逻辑：
| 代码块          | 主要代码                                      | 作用                              |
| ------------ | ----------------------------------------- | ------------------------------- |
| 1. 导入库       | `import json`、`from openai import OpenAI` | 准备程序要用的工具                       |
| 2. 连接模型      | `client = OpenAI(...)`                    | 连接 DeepSeek API                 |
| 3. 定义真实工具    | `def calculator(...)`                     | 写一个真正能执行计算的 Python 工具           |
| 4. 描述工具      | `tools = [...]`                           | 告诉大模型“我有一个 calculator 工具，怎么调用它” |
| 5. Agent 主流程 | `def run_agent(user_input)`               | 控制整个 Agent 怎么运行                 |
| 6. 工具调用流程    | `if tool_calls: ...`                      | 模型想用工具时，Python 执行工具，再把结果交回模型    |
| 7. 测试运行      | `if __name__ == "__main__":`              | 模拟用户提问，看看 Agent 能不能正常工作         |

① 连接大模型
   ↓
② 写真实工具
   ↓
③ 告诉大模型有哪些工具
   ↓
④ 用户提问
   ↓
⑤ 大模型判断要不要用工具
   ↓
⑥ Python执行工具
   ↓
⑦ 工具结果交回大模型
   ↓
⑧ 大模型生成最终答案
