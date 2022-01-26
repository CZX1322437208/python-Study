names0 = ['Alan', 'Jack', 'Peter', 'Tim']
print("Hello", names0[0])

# 嘉宾名单
names = ['tjl', 'tjl', 'tjl']
# 添加嘉宾
names.insert(0, 'TJL')
names.insert(1, 'Tjl')
names.append('tjL')

for name in names:
    print("诚邀" + name + "共进晚餐。")
print(names)
# 缩减名单
while len(names) > 3:
    popped_names = names.pop()
    print("不好意思" + popped_names, "下次一定一起吃饭！")

print(names[2], "您仍在受邀人之列")

del names[1], names[0]

print(names)
