sandwich_orders = ['金枪鱼三明治', '火腿奶酪三明治', '巴沙鱼秋葵厚蛋烧三明治', '鸡胸肉杂菜三明治', '五香烟熏牛肉三明治','aaa','aaa']
finished_sandwich = []

print("aaa没有了")

while 'aaa' in sandwich_orders:
    sandwich_orders.remove('aaa')

print(sandwich_orders)

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    finished_sandwich.append(sandwich_order)
    print(sandwich_order, "已经做好了")

print(finished_sandwich)