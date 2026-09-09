import json
import os
from openai import OpenAI

# 用你的新 API Key 替换下面这行
client = OpenAI(
    api_key="sk-你的新Key",
    base_url="https://api.deepseek.com"
)

# 定义一个工具函数：计算器
def calculator(expression: str) -> str:
    """计算数学表达式，例如 '123 * 456'"""
    try:
        # eval 可以执行简单的数学表达式，这里仅用于演示，实际项目需谨慎
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"计算出错: {e}"

# 工具描述：告诉模型这个工具怎么用
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "计算一个数学表达式，例如 '123 * 456'，返回计算结果",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "要计算的数学表达式"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

def run_agent(user_input):
    # 初始化消息列表，只包含用户输入
    messages = [{"role": "user", "content": user_input}]

    # 第一次调用模型，允许它决定是否调用工具
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        tools=tools,
        tool_choice="auto"  # auto 表示模型自己决定是否调用工具
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    # 如果模型要求调用工具
    if tool_calls:
        # 把模型的回复（包含工具调用请求）加入消息历史
        messages.append(response_message)

        # 遍历所有工具调用（通常一个，但可能多个）
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            # 根据工具名执行对应函数
            if function_name == "calculator":
                result = calculator(function_args["expression"])
            else:
                result = f"未知工具: {function_name}"

            # 把工具执行结果加入消息历史
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": function_name,
                "content": result
            })

        # 再次调用模型，让它根据工具结果生成最终回答
        final_response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages
        )
        return final_response.choices[0].message.content

    # 如果模型没有调用工具，直接返回它的回答
    return response_message.content

# 测试
if __name__ == "__main__":
    question = "帮我算一下 123 * 456"
    print(f"用户：{question}")
    answer = run_agent(question)
    print(f"助手：{answer}")