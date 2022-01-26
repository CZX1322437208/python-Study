active = True
while active:
    i = input("请输入用户名(键入quit以退出)：")
    if i == 'quit':
        active = False
    else:
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(i + "\n")

with open('guest_book.txt') as file_object:
    f = file_object.read()
print(f)
