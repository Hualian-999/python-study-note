# import os

# langchain_community
from langchain_community.chat_models.tongyi import ChatTongyi

# api_key = os.getenv("DASHSCOPE_API_KEY")
# if not api_key:
#     raise ValueError(
#         "请先设置环境变量 DASHSCOPE_API_KEY，示例：setx DASHSCOPE_API_KEY "
#         '"你的API Key"'
#     )

model = ChatTongyi(model="qwen-max")

# 调用invoke向模型提问
res = model.invoke(input="你是谁,能做什么?")

print(res.content)