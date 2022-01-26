current_users = ['admin', 'aaa', 'bbb', 'ccc', 'ddd']
for user in current_users:
    if not current_users:
        print("You need find some users!")
    elif user == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello Jaden,thank you for logging in again.")

current_users_copy = []
for current in current_users:
    current_users_copy.append(current.lower())

new_users = ['000', 'aaa', 'bbb', 'ccc', 'ddd']

for new_user in new_users:
    x = 0
    for current_user in current_users_copy:
        if new_user == current_user:
            x = 1
    if x == 1:
        print("用户名", new_user, "已被使用")
    else:
        print("用户名", new_user, "未被使用")

for new_user in new_users:
    if new_user in current_users_copy:
        print("用户名", new_user, "已被使用")
    else:
        print("用户名", new_user, "未被使用")

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in num:
    if n == 1:
        print('1st')
    elif n == 2:
        print('2nd')
    elif n == 3:
        print('3rd')
    elif n == 4:
        print('4st')
    elif n == 5:
        print('5st')
    elif n == 6:
        print('6st')
    elif n == 7:
        print('7st')
    elif n == 8:
        print('8st')
    elif n == 9:
        print('9st')
