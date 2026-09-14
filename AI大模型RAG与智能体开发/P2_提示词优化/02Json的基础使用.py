import json

d={
    "name": "小明",
    "age": 25,
    "gender": "男"
}

s=json.dumps(d,ensure_ascii=False)
print(s)

l=[
    {
        "name": "小明",
        "age": 25,
        "gender": "男"
    },
    {
            "name": "小红",
            "age": 18,
            "gender": "女"
        },
    {
            "name": "小里",
            "age": 16,
            "gender": "男"
        }
]

print(json.dumps(l,ensure_ascii=False))

json_str='{"name": "小明", "age": 25, "gender": "男"}'
json_arrary_str='[{"name": "小明", "age": 25, "gender": "男"}, {"name": "小红", "age": 18, "gender": "女"}, {"name": "小里", "age": 16, "gender": "男"}]'

res_dict=json.loads(json_str)
print(res_dict,type(res_dict))

res_list=json.loads(json_arrary_str)
print(res_list,type(res_list))