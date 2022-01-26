active = True
where = []

while active:
    place = input("If you could visit one place in the world,where would you go?")
    if place == 'quit':
        print("Thank you for your time.")
        active = False
    else:
        where.append(place)

print(where)