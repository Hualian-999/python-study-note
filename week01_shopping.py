"""week01_shopping.py 极简购物车示例
功能：添加商品、删除商品、查看购物车、退出
使用 list 存储购物车商品
"""

# 初始化购物车，空列表
shopping_cart = []


def show_menu():
	"""打印操作菜单"""
	print("=====简易购物车=====")
	print("1. 添加商品")
	print("2. 删除商品")
	print("3. 查看购物车")
	print("4. 退出程序")
	print("====================")


def add_goods():
	"""添加商品"""
	goods_name = input("请输入要添加的商品名称：")
	shopping_cart.append(goods_name)
	print(f"✅已添加：{goods_name}")


def del_goods():
	"""删除商品"""
	goods_name = input("请输入要删除的商品名称：")
	if goods_name in shopping_cart:
		shopping_cart.remove(goods_name)
		print(f"🗑️已删除：{goods_name}")
	else:
		print(f"❌购物车中没有该商品：{goods_name}")


def show_cart():
	"""展示购物车"""
	if len(shopping_cart) == 0:
		print("🛒购物车是空的！")
	else:
		print("-----你的购物车-----")
		for index, item in enumerate(shopping_cart, start=1):
			print(f"{index}. {item}")
		print("--------------------")


def main():
	"""主循环，程序入口"""
	while True:
		show_menu()
		choice = input("请输入你的选择(1-4)：")
		if choice == "1":
			add_goods()
		elif choice == "2":
			del_goods()
		elif choice == "3":
			show_cart()
		elif choice == "4":
			print("👋程序退出，欢迎下次使用！")
			break
		else:
			print("⚠️输入无效，请输入1-4之间的数字！")
		print()  # 空行，美化输出


if __name__ == "__main__":
	main()
