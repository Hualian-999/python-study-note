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


#需求1：打印一个分割线
# def out_line():
#     print("---------------")
out_line=lambda :print("----------------")
out_line()

# 需求2：计算两个数之和
# def add(x,y):
#     return x+y
add=lambda x,y:x+y
print(add(10,25))

# 需求3：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序
data_list=["C++","C","Python","Jack","PHP","Java","Go","JavaScript","Rust"]
# data_list.sort(key=lambda item:len(item))   #key为sort函数的排序方式，item为列表中的元素
# data_list.sort(key=lambda item:len(item),reverse=True)#reverse=True，排序反转，reverse=False，排序不反转
print(data_list)

# ----------------------------案例--------------------------
# 案例1：计算n的阶乘
# 定义一个函数，根据传入的数字，计算该数字阶乘的结果。
# 分析：
# 8的阶乘: 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1      f(8) = 8 * f(7)
# 7的阶乘: 7 * 6 * 5 * 4 * 3 * 2 * 1      f(7) = 7 * f(6)
# 6的阶乘: 6 * 5 * 4 * 3 * 2 * 1      f(6) = 6 * f(5)
# 5的阶乘: 5 * 4 * 3 * 2 * 1      f(5) = 5 * f(4)
# 4的阶乘: 4 * 3 * 2 * 1      f(4) = 4 * f(3)
# 3的阶乘: 3 * 2 * 1      f(3) = 3 * f(2)
# 2的阶乘: 2 * 1      f(2) = 2 * f(1)
# 1的阶乘: 1      f(1) = 1
# n的阶乘公式: f(n) = n * f(n-1)
# 递归调用（先层层递进，再逐步回归）：指的是在函数中自己调用自己的情况--->一定得有终结点
"""
jc(10)=10*jc(9)                 #先入栈，再出栈
jc(9)=9*jc(8)
jc(8)=8*jc(7)
jc(7)=7*jc(6)=7*720=5040
jc(6)=6*jc(5)=6*120=720
jc(5)=5*jc(4)=5*24=120
jc(4)=4*jc(3)=4*6=24
jc(3)=3*jc(2)=3*2=6
jc(2)=2*jc(1)=2*1=2
jc(1)=1
"""
def jc(n):
    if n==1:
        return 1
    else:
        return n*jc(n-1)

result=jc(10)
print(result)

#案例2
# 电商订单计算器
# 定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额。
# 具体规则如下：
# 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
# 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
def calc_order_cost(*args,coupon=0,score=0,express=0):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args: 商品信息（商品名、价格、数量）--->如：("鼠标",188,2),("键盘",388,1)
    :param coupon: 优惠券
    :param score: 积分
    :param express: 运费
    :return: 订单的总金额
    """
    # 订单的总金额=商品总金额-优惠券-积分+运费
    # 1，计算商品总额
    total_price=[goods[1]*goods[2] for goods in args]
    total_cost=sum(total_price)
    # 2，扣减优惠券
    if total_cost>=5000 and coupon<total_cost:
        total_cost-=coupon
    # 3，扣减积分
    if total_cost>=5000 and score//100 <total_cost:
        total_cost-=score//100
    # 4，添加运费
    total_cost+=express

    return total_cost

# 测试
# total=calc_order_cost(("鼠标",188,2),("键盘",388,1),("手机",3999,1),coupon=10,score=4000,express=9.9)
# print(total)

# total=calc_order_cost(("鼠标",188,2),("键盘",388,1),("手机",6999,1),coupon=10,score=4000,express=9.9)
# print(total)

total=calc_order_cost(("鼠标",188,2),("键盘",388,1),("手机",6999,1),express=9.9)
print(total)
