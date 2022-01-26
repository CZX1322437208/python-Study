# 放眼世界
tourism = ['Shenzhen', 'Chaozhou', 'Yangjiang', 'Zhanjiang', 'Guangzhou']

tour = [x.lower() for x in tourism]

tour = list(map(lambda x: x.lower(), tourism))
# map()函数将传入的函数依次作用到序列的每个元素，并把结果作为新的iterator返回。
# 关键字 lambda 表示匿名函数，冒号前面的 x 表示函数参数

print(tour)

tour.sort()
print(tour)

tour.sort(reverse=True)
print(tour)

tour.reverse()
print(tour)

tour.reverse()
print(tour)
