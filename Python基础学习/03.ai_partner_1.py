import streamlit as st
import os
from openai import OpenAI


st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="👻",
    # 布局
    layout="wide",
    # 控制的是侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("AI智能伴侣")

# logo 待补充

# 系统提示词
system_prompt = "你是一名非常沙雕的AI助理,你叫蓝色大肥鱼,请你使用很跳脱的语气回答用户的问题"

# 初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 展示历史消息
for message in st.session_state.messages:#{"role": "user", "content": "你好"}, {"role": "assistant", "content": "你好呀,我是蓝色大肥鱼,很高兴为你服务~"}
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])

# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量的名字,值就是deepseek的api_key的值)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

# 消息输入框
prompt=st.chat_input("请输入消息内容")
if prompt:  #字符串会自动转换为布尔值,如果字符串费控,则为True,否则为False
    st.chat_message("user").write(prompt)
    print("----------->调用AI大模型,提示词:",prompt)
    # 保存用户输入的消息到会话状态中
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用AI大模型,获取响应
    # 与AI大模型交互()
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果
    print("<------大模型返回的结果:", response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
    # 保存AI大模型返回的结果到会话状态中
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})