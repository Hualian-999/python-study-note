# 采用面向对象编程思想完成如下需求
# 采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
# 系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
# 1．添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2．修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3．删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4．查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 5．退出购物车

# 商品类
class GoodsInfo:
    def __init__(self, name, price, quantity):#待解决:输入数量int,否则报错
        """
        定义商品信息,包括名称,价格,数量
        :param name: 商品名称
        :param price: 商品价格
        :param quantity: 商品数量
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"商品名称：{self.name}，商品价格：{self.price}，商品数量：{self.quantity}"

    def update_goods_info(self, price=None, quantity=None):
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity


# 购物车管理系统类
class CartManagement:
    system_version="1.0"
    system_name="购物车管理系统"

    def __init__(self):
        self.goods_list=[] #列表,记录商品的信息

    # ----------------工具函数：输入校验----------------
    def get_valid_price(self, prompt):
        # 获取合法价格：大于0的int/float，输入错误循环重输
        while True:
            s = input(prompt)
            try:
                price = float(s)
                if price > 0:
                    return price
                else:
                    print("价格必须大于0，请重新输入！")
            except ValueError:
                print("价格输入无效，请输入数字！")

    def get_valid_quantity(self, prompt):
        # 获取合法数量：正整数
        while True:
            s = input(prompt)
            try:
                qty = int(s)
                if qty > 0:
                    return qty
                else:
                    print("数量必须是大于0的整数，请重新输入！")
            except ValueError:
                print("数量输入无效，请输入正整数！")

    # 1.添加购物车
    def add_goods(self):
        name=input("请输入要添加的商品名称:")

        # 判断商品是否已存在,如果存在则不添加
        for i in self.goods_list:
            if i.name==name:
                print("该商品已存在,添加失败!")
                return

        #方式一--->存在bug,无法处理输入非大于0的数字的情况
        # price=float(input("请输入要添加的商品价格:"))
        # quantity=int(input("请输入要添加的商品数量:"))
        #
        # # 判断输入信息是否合理
        # if price>0 and quantity>0:
        #     goods=GoodsInfo(name,price,quantity)
        #     self.goods_list.append(goods)
        #     print("商品信息添加成功~")
        # else:
        #     print("商品价格和数量必须大于0!")

        # 方式二:使用校验函数获取价格、数量--->拓展
        price = self.get_valid_price("请输入要添加的商品价格:")
        quantity = self.get_valid_quantity("请输入要添加的商品数量:")

        goods = GoodsInfo(name, price, quantity)
        self.goods_list.append(goods)
        print("商品信息添加成功~")

    # 2.修改购物车
    def update_goods(self):
        name = input("请输入要修改的商品名称:")

        for i in self.goods_list:
            if i.name==name:
                print(f"当前商品信息:{i}")

                #方式一--->存在bug,无法处理输入非正整数的情况
                # price = float(input("请输入要修改的商品价格:"))
                # quantity = int(input("请输入要修改的商品数量:"))
                # # 判断输入信息是否合理
                # if price > 0 and quantity > 0:
                #     i.update_goods_info(price,quantity)
                #     print("商品修改添加成功~")
                #     print(f"最新商品信息:{i}")
                #     return
                # else:
                #     print("商品价格和数量必须大于0!")
                #     return

                # 方式二:使用校验函数-->拓展
                price = self.get_valid_price("请输入要修改的商品价格:")
                quantity = self.get_valid_quantity("请输入要修改的商品数量:")

                i.update_goods_info(price, quantity)
                print("商品修改添加成功~")
                print(f"最新商品信息:{i}")
                return
        print("该商品不存在,修改失败!")
    # 3.删除购物车
    def del_goods(self):
        name = input("请输入要删除的商品名称:")

        for i in self.goods_list:
            if i.name == name:
                self.goods_list.remove(i)
                print("商品删除成功~")
                return
        print("未找到该商品,删除失败!")
    # 4.查询购物车
    def list_goods(self):
        if len(self.goods_list)==0:
            print("购物车为空~")
            return

        for i in self.goods_list:
            print(i)

    #运行系统
    def run(self):
        print(f"欢迎进入购物车管理系统~当前版本v{CartManagement.system_version}")

        while True:
            print()
            print("#########################################################")
            print("# 1.添加商品 2.修改商品信息 3.删除商品 4.查询商品信息 5.退出系统 #")
            print("#########################################################")
            print()

            choice=input("请选择要执行的操作,输入1-5:")
            match choice:
                case "1": #添加商品
                    self.add_goods()
                case "2": #修改商品信息
                    self.update_goods()
                case "3": #删除商品
                    self.del_goods()
                case "4": #查询商品信息
                    self.list_goods()
                case "5": #退出系统
                    print("已退出系统~")
                    break
                case _: #其他操作
                    print("输入错误,请输入1-5!")


# 测试
if __name__=="__main__":
    shopping_cartmanagement=CartManagement()
    shopping_cartmanagement.run()