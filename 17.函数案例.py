# 案例
# 1.定义一个函数:根据传入的底和高计算三角形面积的函数
# def triangle_area(a,h):
#     """
#     根据传入的底和高计算三角形面积
#     :param a: 底长
#     :param h: 高
#     :return: 三角形面积
#     """
#     area=a*h/2
#     return area
#
# tl=triangle_area(12,15)
# print("底长12,高15的三角形面积:",tl)
#
#
# # 2.定义一个函数:计算传入的字符串中元音字母的个数(元音字母为aeiouAEIOU)
# def aeiou(s):
#     """
#     计算传入的字符串中元音字母的个数
#     :param s: 字符串
#     :return: 元音字符的个数
#     """
#     num=0
#     for w in s:
#         if w in 'aeiouAEIOU':
#             num+=1
#     return num
# print(aeiou("Hello World Hello Python OK"))
#
#
# # 3.定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分,最低分,平均分(保留一位小数)
# def cala_list(score_list):
#     """
#     计算传入的班级学员高考成绩列表中成绩的最高分,最低分,平均分
#     :param score_list: 成绩列表
#     :return: 最高分,最低分,平均分
#     """
#     max_score=max(score_list)
#     min_score=min(score_list)
#     avg_score=round(sum(score_list)/len(score_list),1)
#     return max_score,min_score,avg_score
#
# s_list=[456,654,643,567,589,670,688]
# max_score,min_score,avg_score=cala_list(s_list)
#
# print("最高分:",max_score)
# print("最低分:", min_score)
# print("平均分:",avg_score)


# 练习,完成下列需求
# 1．定义一个函数，根据传入的分数，计算对应的分数等级并返回。
# - 分数 >= 90: A
# - 分数 >= 75: B
# - 分数 >= 60: C
# - 分数 < 60: D

# def level_score(s):
#     """
#     根据传入的分数，计算对应的分数等级并返回
#     :param s: 传入分数
#     :return: 等级
#     """
#     if s>=90:
#         level="A"
#     elif s>=75:
#         level="B"
#     elif s>=60:
#         level="C"
#     else:
#         level="D"
#     return level
# s_level_score=level_score(67)
# print("67对应的等级为:",s_level_score)   #正确

# 2．定义一个函数，用于判断一个字符串是否是回文串，返回 bool 值。
# - 把字符串反转，如果和原字符串相同，就是回文串。（如："level", "radar", "黄山落叶松叶落山黄"）
# def is_palindrome(s):     #palindrome---回文
#     """
#     判断一个字符串是否是回文串，返回 bool 值
#     :param s: 传入的字符串
#     :return: bool 值
#     """
#     reverse_s=s[::-1]          #字符串反转
#     return s==reverse_s
#
# palindrome1=is_palindrome("abcdcba")
# print(palindrome1)


# 3．定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。
# def time_return(s):
#     """
#     将传入的秒转换为小时、分钟、秒
#     :param s: 传入的秒数
#     :return: 小时、分钟、秒
#     """
#     m=round(s/60,1)
#     h=round(m/60,1)
#     return h,m,s
#
# h1,m1,s1=time_return(6543)
# print("6543秒等于:",h1,"小时;",m1,"分钟;",s1,"秒")    #理解错误,将x秒转化为y:z:w计时法
# 优化版
# def time_return(total_sec):
#     """
#     将传入的秒转换为小时、分钟、秒
#     :param total_sec: 传入的总秒数
#     :return: 小时、分钟、秒
#     """
#     h = total_sec // 3600   #整除,先计算有几个小时
#     remain = total_sec % 3600   #remain 为小时后的分钟数
#     m = remain // 60     #整除,计算有多少分钟
#     s = remain % 60    #取模,计算多少秒
#     return h, m, s

# h1,m1,s1=time_return(6543)
# print(f"6543秒等于: {h1}:{m1}:{s1}")


# 4．定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）
# def triangle_type(a,b,c):
#     """
#     判定三角形的类型
#     :param a: 边长1
#     :param b: 边长2
#     :param c: 边长3
#     :return: 三角形类型
#     """
#     if a+b<=c:   #仅判断了一种情况,忽略了b+c<=a or a+c<=b
#         tr_type="不能构成三角形"
#     else:
#         if a==b==c:
#            tr_type="等边三角形"
#         elif a==b or b==c or c==a:
#             tr_type="等腰三角形"
#         else:
#             tr_type="普通三角形"
#     return tr_type
#
# triangle_type1=triangle_type(21,21,44)
# print(triangle_type1)
# 优化版
# def triangle_type(a,b,c):
#     """
#     判定三角形的类型
#     :param a: 边长1
#     :param b: 边长2
#     :param c: 边长3
#     :return: 三角形类型
#     """
#     # 三角形条件：任意两边之和大于第三边
#     if a+b>c and a+c>b and b+c>a:
#         if a==b==c:
#            tr_type="等边三角形"
#         elif a==b or b==c or c==a:
#             tr_type="等腰三角形"
#         else:
#             tr_type="普通三角形"
#     else:
#         tr_type="不能构成三角形"
#     return tr_type

# triangle_type1=triangle_type(21,3,4)
# print(triangle_type1)

# ---------------字符串常用方法-----------------
# find()  在字符串中查找子串，返回第一次出现的索引位置，找不到返回-1
# s.find('Python')
# count()  统计在字符串中出现的次数
# s.count('H')
# upper()   将字符串中的所有字母转换为大写
# s.upper()
# lower()   将字符串中的所有字母转换为小写
# s.lower()
# split()   将字符串按指定分隔符分隔成列表
# s.split(' ')
# strip()   去除字符串两端的空白字符或指定字符
# s.strip()/s.strip('*')
# replace()  将字符串中的指定子串替换为新的字串
# s.replace('H','C')
# startswith()   检查字符串是否以指定子串开头，返回布尔值
# s.startswith('P')

# s = "    Hello-Python-Hello-World    "
# # find()查找指定字符串第一次出现的索引位置
# index = s.find("-")
# print(index)

# # count()统计子字符串在指定字符串中出现的次数
# c = s.count("o")
# print(c)

# # upper()转为大写
# su = s.upper()
# print(su)

# # lower()转小写
# sl = s.lower()
# print(sl)

# # split()将字符串按照指定字符串切割-列表
# slist = s.split("-")
# print(slist)

# # strip()去除字符串两端的空格
# ss = s.strip()
# print(ss)

# replace()将字符串中的指定字串替换为新的内容
# sr=s.replace(_old:"-",_new:"_")   #报错
# sr = s.replace("-", "_")
# print(sr)

# startswith()/endswith() 判断字符串是否以指定的字符串开头/结尾，返回布尔值
# print(s.startswith("Hello"))
# print(s.endswith("Python"))

# 案例1：邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个.），如果输入正确，输出“邮箱格式正确”，否则输出“邮箱格式错误”
# 方式一
# 1.接收用户输入的邮箱
# mail = input("请输入邮箱：")
# # 2.判断邮箱的格式
# if mail.count("@") == 1 and mail.count(".") >= 1:
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")

# 方式二：in 运算符--->判断字串是否存在字符串中，存在，返回True；否则，返回False
# 1.接收用户输入的邮箱
# mail = input("请输入邮箱：")
# # 2.判断邮箱的格式
# if mail.count("@") == 1 and "." in mail:
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")

# 练习1.输入一个字符串，判断该字符串是否是回文
# 黄山落叶松叶落山黄
# 上海自来水来自海上
# 自主练习：
# s=input("请输入一句话：")
# list1=[]
# for i in s:
#     list1.append(i)
# list1.reverse()
# if list1==list1.reverse():      #`.reverse()` 是**原地修改列表**，返回值是 `None`，不能用来做等于比较。`list1==None`永远不成立
#     print(f"{s}是回文")    #错误

# 优化版
# s = input("请输入一句话：")
# # s[::-1] 直接得到反转后的字符串
# if s == s[::-1]:
#     print(f"{s}是回文")
# else:
#     print(f"{s}不是回文")

# 练习2.将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来
# 自主练习
list1 = []
for i in range(10):
    s = input("请输入一个字符：")
    s2 = s[::-1]
    s3 = s2.upper()
    list1.append(s3)
print(list1)

for j in list1:
    print(j)     #正确

# 简化版
# list1 = []
# for i in range(10):
#     s = input("请输入一个字符串：")
#     # 一行完成：先反转s，再转大写
#     res = s[::-1].upper()
#     list1.append(res)

# print(list1)
# for j in list1:
#     print(j)

# 极简版
# list1 = [input("请输入一个字符串：")[::-1].upper() for _ in range(10)]
# print(list1)
# for j in list1:
#     print(j)
