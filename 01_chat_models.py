# 直接把 API Key 写在代码里（临时测试用，最稳定）
import os
from openai import OpenAI

# 阿里云配置
QWEN_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
QWEN_CHAT_MODEL = "qwen-plus"

# 直接填你的 Key（我已经帮你放进去了！）
api_key = "sk-9efda359aae642f4aeeb262f5f2127c7"

if not api_key:
    raise RuntimeError("没有读取到 DASHSCOPE_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url=QWEN_BASE_URL,
)

completion = client.chat.completions.create(
    model=QWEN_CHAT_MODEL,
    messages=[
        {"role": "system", "content": "你是自然语言处理课程助教，回答要准确、简洁。"},
        {"role": "user", "content": "请用三句话解释什么是自然语言处理。"},
    ],
    temperature=0.3,
)

answer = completion.choices[0].message.content
print(answer)