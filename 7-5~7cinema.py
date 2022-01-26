
active = True

x = input("是否进行查询？(y/n)：")
if x == 'y':
    while active:
        age = input("请输入观影人年龄：")
        if age=='quit':
            print("查询结束")
            break
        else:
            age = int(age)
            if 0 < age < 3:
                print("电影票价：免费")
            elif 3 < age < 12:
                print("电影票价：10块")
            elif 12 < age < 100:
                print("电影票价：15块")
else:
    print("查询结束")
