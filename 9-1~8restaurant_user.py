class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def discribe_restaurant(self):
        print(f"餐馆名称是：{self.restaurant_name},类型为：{self.cuisine_type}。")

    def open_restaurant(self):
        print("餐馆正常营业中")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


a_restaurant = Restaurant('AAA', 'aaa')
a_restaurant.discribe_restaurant()
a_restaurant.open_restaurant()
a_restaurant.set_number_served(10)
print(f"当前就餐人数为：{a_restaurant.number_served}")
a_restaurant.increment_number_served(20)
print(f"每天可接待就餐人数为：{a_restaurant.number_served}")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['aaa', 'bbb', 'ccc']

    def show(self):
        print(f"冰淇淋口味有：{self.flavors}")


ice = IceCreamStand('A', 'B')
ice.show()


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"fist_name:{self.first_name},last_name:{self.last_name}")

    def greet_user(self):
        name = self.first_name + self.last_name
        print(f"Hello,{name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


a_user = User('a', 'b')
a_user.describe_user()
a_user.greet_user()
a_user.increment_login_attempts()
print(a_user.login_attempts)
a_user.reset_login_attempts()
print(a_user.login_attempts)


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"管理员权限有：{self.privileges}")


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        #    self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = Privileges()

    def show_privileges(self):
        self.privileges.show_privileges()


admin = Admin('A', 'B')
admin.show_privileges()


