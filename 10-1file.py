filename = 'C:/desktop/test.txt'
with open(filename) as file_object:  # 默认只读
    f = file_object.read()
print(f)

with open(filename, 'w') as file_object:  # 写入(清空原文件后重写，文件不存在时创建)
    f = file_object.write("aaa\n")

with open(filename, 'a') as file_object:  # 附加模式(在原文件基础上添加，而不是覆盖)
    f = file_object.write("bbb\n")

with open(filename, 'r+') as file_object:  # 读写
    f = file_object.read()
