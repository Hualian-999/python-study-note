# 函数进阶2

# 函数的参数类型
# 普通参数：数字，布尔，字符串，列表，元组，集合，字典等
# 特殊参数：函数

# 加
def add(x, y):
    return x + y


# 减
def subtract(x, y):
    return x - y


# 乘
def multiply(x, y):
    return x * y


# 除
def divide(x, y):
    return x / y


# 计算
def calc(x, y, oper):  # oper只能调用函数
    return oper(x, y)


print(calc(10, 20, divide))

# 匿名函数：没有名称的函数，需要通过lambda表达式来声明函数，可简化简单函数的编写
# 格式：lambda 参数列表:函数体
# def 定义的函数叫命名函数
# 注意，函数逻辑比较简单且只在一个地方使用时，可以考虑使用匿名函数，简化书写（通常作为高阶函数的参数使用）
# 匿名函数中可以返回结果，也可以不返回结果，返回结果时，不需要写return，表达式的运行结果就是要返回的结果

print(calc(10, 20, lambda x, y: x + y))