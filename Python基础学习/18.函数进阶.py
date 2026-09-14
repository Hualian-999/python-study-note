# 全局变量:在函数外部 或 函数的内部都是可以访问的
# num=100
#
# # 定义函数
# def circle_area(r):
#     # 局部变量:只能在函数内部使用
#     pi=3.14
#     area=pi*r*r
#
#     global num   #声明使用的是全局变量,后赋值,全局变量值随之改变
#     num=10000
#     print("num=",num)
#
#     return area
#
# # 调用函数
# c_area=circle_area(100)
# print(c_area)
#
# print("num=",num)



# global关键字:由于明确告诉python使用的是全局变量(先声明,再使用)
# 注意事项,尽量避免在函数中使用全局变量,因为会使代码难以维护和调试(会改变全局变量的值)
# 考虑使用函数参数和返回值来传递数据,而不是依赖全局变量
# global主要用在程序的状态,配置和计数器等场景中


# -----------------函数-传参方式-----------------
# 定义函数
def reg_stu(name,age,gender,city):
    print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
    return {"name":name,"age":age,"gender":gender,"city":city}

# 传参方式一:位置参数--->实参完全按照形参顺序
stu=reg_stu("张三",18,"男","北京")
print(stu)

# 传参方式二:关键字参数
stu=reg_stu(name="王林",age=28,gender="男",city="北京")
print(stu)

# 传参方式三:位置参数+关键字参数--->位置参数在前,关键字参数在后
stu=reg_stu("韩立",220,city="北京",gender="男")
print(stu)

# 位置参数优点:简介      缺点:可读性差,易出错,维护难     使用场景:参数少(<=3个),且顺序自然
# 关键字参数优点:可读性强,易维护和扩展    缺点:代码繁琐    使用场景:参数多,或易混淆的场景
# 黄金法则:半年后回看今天的代码,能否一眼看出每个参数的含义,如果不能,就使用关键字参数
# ------------------------------# 不定长参数(位置参数*args--->元组）-------------------------------
# 需求：根据传入的这批数据，计算这批数据的最小值，最大值，平均值
# def calc_data(*args):
#     min_data=min(args)
#     max_data=max(args)
#     avg_data=sum(args)/len(args)
#     return min_data,max_data,round(avg_data,1)

# # 调用函数
# data=calc_data(10,20,30,40,50,60,70,80,90,100)   #数据会封装到args中
# print(data)

# data=calc_data(100,200,300,400,500)
# print(data)

# 注意：传递的所有匹配的位置参数都会背args变量收集，这些参数会合并封装为一个元组，args是元组类型（并不会封装关键字参数）
# 注意：args只是约定俗成的变量名，并不是关键字，这里可以使用任何合法的变量名（如*data)

# ------------------------------# 不定长参数(关键字参数**kwargs--->字典）-------------------------------
# 定义函数
def calc_data(*args,**kwargs):
    """
    据传入的这批数据，计算这批数据的最小值，最大值，平均值
    :param args: 不定长位置参数，需要计算的这批数据
    :param kwargs: 不定长关键字参数
    round：保留的小数位个数
    print：是否打印输出
    :return: 最小值，最大值，平均值
    """
    min_data=min(args)
    max_data=max(args)
    avg_data=sum(args)/len(args)

    if kwargs.get('round') is not None:#如果round对应的值存在
        avg_data=round(avg_data,kwargs.get('round'))

    if kwargs.get('print'):#如果print值为True
        print(f"计算出来的最小值：{min_data},最大值：{max_data},平均值：{avg_data}")

    return min_data,max_data,avg_data

# 调用函数
# data=calc_data(2,7,9,10,45,round=2,print=True)   #数据会封装到args中
# print(data)

data=calc_data(2,7,9,10,45,33,11,28,91,32,75,49,round=3)
print(data)

# 注意：参数是以：”键=值“形式传递的关键字参数，这些”键=值“参数都会被kwargs接受，并合并封装为一个字典类型
# 注意：kwargs只是约定俗成的变量名，并不是关键字，这里可以使用任何合法的变量名（如**options)
# *args适用于处理数量不确定的数据
# **kwargs适用于处理数量不确定的选项（函数的配置参数，用来定制函数的行为）
# 上述两者同时存在时，先写不定长位置参数，再写不定长关键字参数
# 核心数据：你要什么
# 点奶茶("珍珠奶茶")
# 选项：你要什么样的
# 点奶茶("珍珠奶茶",甜度="少糖",加料=["布丁","珍珠"],大小="大杯")
