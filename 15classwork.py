def number(t, r):
    print(t * r)

item = input("Введите символ или слово: ")
n = int(input("Введите кол-во символов: "))
number(item, n)

def describe_pet(animal_type, pet_name):
    print(f"\nУ меня есть {animal_type}.")
    print(f"Мой {animal_type} и его зовут {pet_name.title()}.")

describe_pet("хомяк", "Гарри")
describe_pet("собака", "Вилли")
print("\n")

def user(name, surname, age) :
    r = f"\tЕго зовут {name}, \n\tЕго фамилия {surname},\n\tЕму {age}"
    return r
user_name = input("Введите имя:")
user_surname = input("Введите фамилию:")
user_age = input("Введите возраст:")

result = user(user_name, user_surname, user_age)
print(result)
