#1
def display_message(number):
    print(f"Вы получили {number} подарков\n")
i = 5
display_meassage(i)

#2
def favourite_book(name):
    print(f"One of my favourite book is {name}\n")
n = "Amphibian man"
favourite_book(n.title())

#3
def make_shirt(size, text):
    print(f"Размер футболки - '{size}'. Текст - '{text}'\n")
x = "L"
y = "I Love Python"
make_shirt(x, y)
a = input("Размер футболки: ")
b = input("Текст на футболке: ")
make_shirt(a, b)

#4
def describe_city(city, country="Geramny"):
    print(f"{city} is in {country}")

describe_city("Kyiv", "Ukraine")
describe_city("Moscow", "Russia")
describe_city("Munich")
