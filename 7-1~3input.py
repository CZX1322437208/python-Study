message1 = input("你想要啥车？")
print("噢，原来你想要" + message1 + "\n")

message2 = input("几个人吃饭呐？")
message2 = int(message2)
if message2 > 8:
    print("没空桌了，等等吧。")
elif 0 < message2 <= 8:
    print(f"贵宾{message2}位里面请!\n")
elif message2 == 0:
    print(f"鬼宾1位里面请!\n")

message3 = input("输个数吧：")
message3 = int(message3)
if message3 % 10 == 0:
    print("是10的倍数")
else:
    print("不是10的倍数")
