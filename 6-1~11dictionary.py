person_information = {'first_name': 'Tang', 'last_name': 'Jialu', 'age': '20', 'city': 'Zhanjiang'}
print(person_information)

for k, v in person_information.items():
    print(k, ".", v)

print(person_information.keys())
print(person_information.values())

person_information2 = {'first_name': 'Chen', 'last_name': 'Zhenxuan', 'age': '21', 'city': 'Shenzhen'}
person_information3 = {'first_name': 'Lu', 'last_name': 'Mingminng', 'age': '20', 'city': 'Zhanjiang'}

people = [person_information, person_information2, person_information3]

for p in people:
    for i in p.values():
        print(i)

cities = {'Shenzhen': {'country': 'China', 'population': '3', 'fact': 'money'},
          'Yangjiang': {'country': 'China', 'population': '7', 'fact': 'cards'},
          'Chaozhou': {'country': 'China', 'population': '5', 'fact': 'sleep'}}

for k,v in cities.items():
    print(f"\nCity_name:{k}")
    print(v)

