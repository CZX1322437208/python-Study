def make_pizza(size, *toppings):
    print(f"Making a {size}-inch pizza with the following toppings:")
    for top in toppings:
        print(f"- {top}")


make_pizza(16, 'pepperoni')


def make_sandwich(*args):
    print("配料有：")
    for a in args:
        print(a)


make_sandwich('aaa', 'bbb', 'ccc')


def build_profile(surname, name, **user_info):
    user_info['surname'] = surname
    user_info['name'] = name
    return user_info


user_profile = build_profile('Chen', 'Zhenxuan', location='Shenzhen')
print(user_profile)


def build_carfile(manufacturer, model, **car_file):
    car_file['manufacturer'] = manufacturer
    car_file['model'] = model
    return car_file


car = build_carfile('subaru', 'outback', color='blue', tow_package=True)
print(car)
