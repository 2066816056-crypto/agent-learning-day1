from openai import OpenAI

# 把下面的 "sk-xxxx" 替换成你的新 API Key
client = OpenAI(
    api_key="sk-你的新Key",
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个乐于助人的助手。"},
        {"role": "user", "content": "你好，请介绍一下你自己，用一句话。"}
    ]
)

print(response.choices[0].message.content)