import os
from langchain_openai import ChatOpenAI


def call_llm(user_input: str) -> str:
    """调用 DeepSeek 模型并返回文本回复。"""
    llm = ChatOpenAI(
        model="deepseek-chat",
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com"
    )
    result = llm.invoke(user_input)
    return result.content


if __name__ == "__main__":
    answer = call_llm("你好，请用一句话介绍自己")
    print(answer)