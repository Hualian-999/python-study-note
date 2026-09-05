text = input("请输入一段文字：")
count_dict = {}

for char in text:
	if char in count_dict:
		count_dict[char] += 1
	else:
		count_dict[char] = 1

print("字符统计结果：")
for k, v in count_dict.items():
	print(f"字符【{k}】：出现{v}次")
