# from openai import OpenAI
# import json


# client = OpenAI(
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
# )

# schema=['日期','股票名称','开盘价','收盘价','成交量']
# examples_data = [   # 示例数据
#     {
#         "content": "2023-01-10，股市震荡。股票强大科技A股今日开盘价100人民币，一度飙升至105人民币，随后回落至98人民币，最终以102人民币收盘，成交量达到520000。",
#         "answers": {
#             "日期": "2023-01-10",
#             "股票名称": "强大科技A股",
#             "开盘价": "100人民币",
#             "收盘价": "102人民币",
#             "成交量": "520000"
#         }
#     },
#     {
#         "content": "2024-05-16，股市利好。股票英伟达美股今日开盘价105美元，一度飙升至109美元，随后回落至100美元，最终以116美元收盘，成交量达到3560000。",
#         "answers": {
#             "日期": "2024-05-16",
#             "股票名称": "英伟达美股",
#             "开盘价": "105美元",
#             "收盘价": "116美元",
#             "成交量": "3560000"
#         }
#     }
# ]
# questions = [   # 提问问题
#     "2025-06-16，股市利好。股票传智教育A股今日开盘价66人民币，一度飙升至70人民币，随后回落至65人民币，最终以68人民币收盘，成交量达到123000。",
#     "2025-06-06，股市利好。股票黑马程序员A股今日开盘价200人民币，一度飙升至211人民币，随后回落至201人民币，最终以206人民币收盘。"
# ]

# """
# [
# {"role": "system", "content": f"你帮我完成信息抽取，我给你句子，你抽取{schema}信息，按JSON字符串输出，如果某些信息不存在，用'原文未提及'表示，请参考如下示例："},
# {"role": "user", "content": "2023-01-10，股市震荡。股票强大科技A股今日开盘价100人民币，一度飙升至105人民币，随后回落至98人民币，最终以102人民币收盘，成交量达到520000。"},
# {"role": "assistant", "content": '{"日期":"2023-01-10","股票名称":"强大科技A股","开盘价":"100人民币","收盘价":"102人民币","成交量":"520000"}'},
# {"role": "user", "content": "2024-05-16，股市利好。股票英伟达美股今日开盘价105美元，一度飙升至109美元，随后回落至100美元，最终以116美元收盘，成交量达到3560000。"},
# {"role": "assistant", "content": '{"日期":"2024-05-16","股票名称":"英伟达美股","开盘价":"105美元","收盘价":"116美元","成交量":"3560000"}'},
# {"role": "user", "content": f"按照上述示例，现在抽取这个句子的信息：{要抽取的句子文本}"}
# ]
# """

# messages = [
#     {"role": "system", "content": f"你帮我完成信息抽取，我给你句子，你抽取{schema}信息，按JSON字符串输出，如果某些信息不存在，用'原文未提及'表示，请参考如下示例："}
# ]

# for example in examples_data:
#     messages.append(
#         {"role": "user", "content": example["content"]}
#     )
#     messages.append(
#         {"role": "assistant", "content": json.dumps(example["answers"], ensure_ascii=False)}
#         )

# for q in questions:
#     response = client.chat.completions.create(
#         model="qwen3.8-max",
#         messages=messages + [{"role": "user", "content": f"按照上述示例，现在抽取这个句子的信息：{q}"}]
#     )
    
#     print(response.choices[0].message.content)


# 练习
"""
彩票信息抽取作业

有如下 5 条文本，需要抽取信息：
1．2025 年第 100 期，开好红球 22 21 06 01 03 11 篮球 07，一等奖中奖为 2 注。
2．2025101 期，有 3 注 1 等奖，10 注 2 等奖，开号篮球 11，中奖红球 3、5、7、11、12、16。

期待经过通过模型抽取信息得到如下结果：
1．{"期数": "2025100", "中奖号码": [1, 3, 6, 11, 21, 22, 7], "一等奖": "2 注"}
2．{"期数": "2025101", "中奖号码": [3, 5, 7, 11, 12, 16, 11], "一等奖": "3 注"}

请设计 Prompt，基于 FewShot，对模型做示例的提示，得到需要的结果。
"""

from openai import OpenAI
import json


client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

caipiao_schema = ["期数", "中奖号码", "一等奖"]
example_data = [
    {"content": "2025 年第 100 期，开好红球 22 21 06 01 03 11 篮球 07，一等奖中奖为 2 注。",
        "answers": {
            "期数": "2025100", 
            "中奖号码": [1, 3, 6, 11, 21, 22, 7],
            "一等奖": "2 注"}
    },
    {
        "content": "2025101 期，有 3 注 1 等奖，10 注 2 等奖，开号篮球 11，中奖红球 3、5、7、11、12、16。",
        "answers": {
            "期数": "2025101", 
            "中奖号码": [3, 5, 7, 11, 12, 16, 11], 
            "一等奖": "3 注"}
    }
]
questions = [
    "2025 年第 102 期，开好红球 05 12 18 22 25 30 篮球 09，一等奖中奖为 1 注。",
    "2025103 期，有 2 注 1 等奖，5 注 2 等奖，开号篮球 08，中奖红球 4、8、15、16、23、42。"]
"""
[
{"role": "system", "content": f"你帮我完成彩票信息抽取，我给你句子，你抽取{caipiao_schema}信息，按JSON字符串输出，如果某些信息不存在，用'原文未提及'表示，请参考如下示例："},
{"role": "user", "content": "2025 年第 100 期， 开好红球 22 21 06 01 03 11 篮球 07，一等奖中奖为 2 注。"},
{"role": "assistant", "content": '{"期数": "2025100", "中奖号码": [1, 3, 6, 11, 21, 22, 7], "一等奖": "2 注"}'},
{"role": "user", "content": "2025101 期，有 3 注1等奖，10 注 2 等奖，开号篮球 11，中奖红球 3、5、7、11、12、16。"},
{"role": "assistant", "content": '{"期数": "2025101", "中奖号码": [3, 5, 7, 11, 12, 16, 11], "一等奖": "3 注"}'},
{"role": "user", "content": f"按照上述示例，现在抽取这个句子的信息：{要抽取的句子文本}"}
]
"""

messages = [
    {"role": "system", "content": f"你帮我完成彩票信息抽取，我给你句子，你抽取{caipiao_schema}信息，按JSON字符串输出，如果某些信息不存在，用'原文未提及'表示，请参考如下示例："}
]

for example in example_data:
    messages.append(
        {"role": "user", "content": example["content"]}
    )
    messages.append(
        {"role": "assistant", "content": json.dumps(example["answers"], ensure_ascii=False)}
    )
for q in questions:
    response = client.chat.completions.create(
        model="qwen3.8-max",
        messages=messages + [{"role": "user", "content": f"按照上述示例，现在抽取这个句子的信息：{q}"}]
    )
    
    print(response.choices[0].message.content)