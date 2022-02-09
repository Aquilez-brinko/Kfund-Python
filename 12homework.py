#1
a = {
    "first_name": "Никита",
    "last_name": "Трунов",
    "age": "16",
    "city": "Харьков"
}
for i in a.items():
    print(i)
print("\n")

#2
a = {
    "Паши": "5",
    "Ромы": "2",
    "Никиты": "1",
    "Артема": "8"
}
for b, c in a.items():
    print(f"Любимое число {b}: {c} ")
print("\n")

#3
a = {
    "str": "строка",
    "int": "целые числа",
    "lists": "списки",
    "boolean": "логический тип данных",
    "float": "число с плавающей точкой"
}
for b, c in a.items():
    print(f"{b}: {c} ")
print("\n")

#4
a = {
    "str": "строка",
    "int": "целые числа",
    "lists": "списки",
    "boolean": "логический тип данных",
    "float": "число с плавающей точкой",
    "range": "диапазон",
    "bytes": "байты",
    "print": "вывести строку",
    "while": "условие с цыклом",
    "if": "условие"
}
for b, c in a.items():
    print(f"{b}: {c} ")
print("\n")

#5
a = {
"Нил": "Египет",
"Волга": "Россия",
"Луар": "Франция"
}
for b, c in a.items():
    print(f"{b}: {c} ")
for x in a.keys():
    print(f"{x} ")
for x in a.values():
    print(f"{x} ")
print("\n")

#6
language = {
    "Артем":"python",
    "Никита":"c++",
    "Тимур":"с#",
    "Егор":"js",
    "Юра":"C+",
    }
people = {
    "Артем",
    "Никита",
    "Тимур",
    "Егор",
    "Юра",
    "Ваня"
}
for i in people:
    if i in language:
            print(f"{i} благодарим за участие! ")
    else:
        print(f"{i} пройдите опрос")
