from langchain_openai import ChatOpenAI

def call_llm(user_input):
    # 初始化DeepSeek大模型
    llm = ChatOpenAI(
        base_url="https://api.deepseek.com",
        api_key="sk-在这里粘贴你的deepseek密钥",
        model="deepseek-chat"
    )
    # 发送消息获取结果
    response = llm.invoke(user_input)
    return response.content

# 测试调用
if __name__ == "__main__":
    res = call_llm("你好，请简单介绍LangChain")
    print(res)