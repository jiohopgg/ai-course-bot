import os
import numpy as np
from openai import OpenAI

# 你的阿里云密钥
api_key = "sk-9efda359aae642f4aeeb262f5f2127c7"
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"

client = OpenAI(
    api_key=api_key,
    base_url=BASE_URL
)

# 给定4段文本
texts = [
    "我喜欢自然语言处理，尤其是大语言模型。",
    "大模型可以完成文本生成、摘要和问答任务。",
    "今天学校食堂的红烧肉很好吃。",
    "语义向量可以用来计算两个句子的相似度。",
]

# 获取文本向量
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-v4",
        input=text
    )
    return response.data[0].embedding

# 余弦相似度
def cosine_similarity(vector_a, vector_b):
    vector_a = np.array(vector_a)
    vector_b = np.array(vector_b)
    return np.dot(vector_a, vector_b) / (
        np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    )

# 批量生成向量
emb_list = [get_embedding(t) for t in texts]

# 1. 两两计算相似度
print("===== 句子两两相似度 =====")
for i in range(len(texts)):
    for j in range(i + 1, len(texts)):
        sim = cosine_similarity(emb_list[i], emb_list[j])
        print(f"句子{i+1} 与 句子{j+1} 相似度：{sim:.4f}")

# 2. 查询：语义向量有哪些作用
query_text = "语义向量有哪些作用"
query_emb = get_embedding(query_text)

# 遍历比对
score_list = []
for emb in emb_list:
    score = cosine_similarity(query_emb, emb)
    score_list.append(score)

max_index = np.argmax(score_list)
print("\n===== 语义检索结果 =====")
print(f"查询语句：{query_text}")
print(f"最相似句子：{texts[max_index]}")
print(f"相似度分数：{score_list[max_index]:.4f}")