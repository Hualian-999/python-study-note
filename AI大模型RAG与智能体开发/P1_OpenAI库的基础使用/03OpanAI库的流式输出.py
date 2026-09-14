from openai import OpenAI
# 1.获取client对象,openAI类对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 2.调用模型
response = client.chat.completions.create(
    model="qwen3.8-max", 
     messages=[{"role": "system", "content": "你是一个Python编程专家,并且不说废话,并且话很多"},
                {"role": "assistant", "content": "好的,我是编程专家,并且话很多,你要问什么"},
                {"role": "user", "content": "输出1-10的数字,使用Python代码"} 
    ],
    stream=True,   #开启流式输出,返回结果会分段返回,每一段都是一个字典,字典中包含delta字段,delta字段中包含content字段,content字段中包含模型输出的内容
)
  

# 3.处理返回结果
# print(response.choices[0].message.content)
for chunk in response:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(
            delta.content,
            end="",      #每一段之间以空格分隔
            flush=True   #立刻刷新缓冲区
        )