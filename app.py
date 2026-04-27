from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from openai import OpenAI

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# 你的 API Key
api_key = "sk-9efda359aae642f4aeeb262f5f2127c7"
base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"

client = OpenAI(api_key=api_key, base_url=base_url)

# 首页
@app.get("/")
def index():
    return FileResponse("static/index.html")

# 聊天接口
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=[{"role": "user", "content": user_message}]
    )
    reply = completion.choices[0].message.content
    return {"reply": reply}