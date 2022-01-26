alien_cloler = 'green'
if alien_cloler == 'green':
    print("player get 5 points.")
elif alien_cloler == 'yellow':
    print("player get 10 points.")
elif alien_cloler == 'red':
    print("player get 15 points.")
else:
    print("player get 0 point.")

age = 21
if age < 2:
    print("baby")
elif 2 <= age < 4:
    print('child')
elif 4 <= age < 13:
    print('children')
elif 13 <= age < 20:
    print('youth')
elif 20 <= age < 65:
    print('adult')
else:
    print('aged')

favorite_fruits = ['banana', 'apple', 'orange', 'pear', 'mango']
if 'mango' in favorite_fruits:
    print("You really like mango!")
if 'mango' not in favorite_fruits:
    print("oh,please try it.")
