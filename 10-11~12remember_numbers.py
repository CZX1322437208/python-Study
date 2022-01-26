import json


def get_numbers():
    filename = 'usernumber.json'
    try:
        with open(filename) as f:
            usernumber = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return usernumber


def favorite_number():
    user_favorite_number = get_numbers()
    if user_favorite_number:
        print(f"I know you favorite number!It is:{user_favorite_number}")
    else:
        user_favorite_number = input("what is your favorite number?:")
        filename = 'usernumber.json'
        with open(filename, 'w') as f:
            json.dump(user_favorite_number, f)
            print("Thank you.")


favorite_number()
