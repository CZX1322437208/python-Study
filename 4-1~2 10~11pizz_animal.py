pizza = ['超级至尊', '经典夏威夷风情', '炙烤牛肉']
for x in pizza:
    print("我喜欢", x, "pizza")
print("I really like pizza!")

anmals = ['🐱', '🐕', '🐹']
for y in anmals:
    print("A", y, "make a great pet.")
print("Any of these animals would make a great pet.")

print("The first three items in the list are:", anmals[0:3])

friend_pizzas=pizza[:]
pizza.append("随便一个")
friend_pizzas.append("随便的另外一个")
print(pizza)
print(friend_pizzas)

food = ("甜品", "汤", "主食", "肉", "菜")
for f in food:
    print(f)

food = ("a", "b", "c")
print(food)
