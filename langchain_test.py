# 测试 langchain 导入是否正常
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

print("✅ Langchain 包导入成功！")

# 简单测试实例化（这里先不调用API，只测试包能否加载，不会消耗token）
try:
    llm = ChatOpenAI(
        base_url="https://api.deepseek.com",
        api_key="sk-xxx", # 这里先随便填，这一步仅测试导入，不会发起请求
        model="deepseek-chat"
    )
    print("✅ ChatOpenAI 加载成功")
except Exception as e:
    # 如果报错是因为api_key无效，不是包安装失败，属于正常现象
    print(f"⚠️ 实例化提示(不用管): {e}")
    print("👉 只要前面两行没有报ModuleNotFoundError，就代表langchain安装成功！")