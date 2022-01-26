
for x in range(1, 21):
    print(x)

numbers = [num for num in range(1, 1_000_001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

ji = [ji for ji in range(1, 21, 2)]
for y in ji:
    print(y)

chu = []
for z in range(3, 30):
    if z % 3 == 0:
        chu.append(z)
for ch in chu:
    print(ch)

li_fang = []
for li in range(1, 11):
    li_fang.append(li ** 3)
for l in li_fang:
    print(l)

lf = [value ** 3 for value in range(1, 11)]
print(lf)
