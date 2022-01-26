def make_shirt(size='XL', word='I love python'):
    print(f"T-shirt 的尺码是{size},上面的字样是{word}")


make_shirt('M', 'ABC')
make_shirt(word='DEF', size='X')
make_shirt()
make_shirt('M')


def describe_city(name='Shenzhen', country='China'):
    print(f"{name} is in {country}")
    return name, country


describe_city()
print(describe_city())
