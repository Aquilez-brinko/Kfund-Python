#1
a = {
     "Google": "90",
     "Opera": "10"
}
print(f"{a}\n")

#2 
lists = { 
    "Cегодня": ["вытеру пыль", "попылесошу"], 
    "Завтра": ["займусь спортом", "cделаю уроки"] 
} 
print("Сегодня: ") 
for a in lists["Cегодня"]: 
    print(a) 
 
print("Завтра: ") 
for a in lists["Завтра"]: 
    print(a) 
print("\n")

#3
a = {
     "232": "Алиса",
     "330": "Юра",
     "280": "Андрей",
     "": "Никита"
}
for i in a:
    if i == "232":
        print("Привет, ", a["232"])
    elif i == "330":
        print("Привет, ", a["330"])
    elif i == "280":
        print("Привет, ", a["280"])
    else:
        print("Привет всем!")
print('\n')
#4
a = {
     "Камень": "15",
     "Дерево": "20"
}
for b, c in a.items():
    print(f"{b}: {c}")
print("\n")

#5
n = int(input("Введите n:"))
n = n + 1
a=1
d = {a: a ** 2 for a in range(n)}
del d[0]
print(f"{d}\n")

#6
a = {
    "Шутер": "CS:GO",
    "Кооператив": "Rainbow Six Siege"
}
for b, c in a.items():
    print(f"Жанр {c} - {b}")
print("\n")

#7
a = {
    "Билл Гейтс": "28 октября 1955",
    "Марк Цукерберг": "14 мая 1984"
}
n=input('Введите имя и фамилию информатика (Билл Гейтс, Марк Цукерберг):')
for i in a:
    if n == "Билл Гейтс":
        print(a["Билл Гейтс"])
        break
    elif n == "Марк Цукерберг":
        print(a["Марк Цукерберг"])
        break
    else:
        print("Ошибка!")
        break
print('\n')

#8
a = {
     "Шоколадка": "Черный шоколад с орехом",
     "Ролл": "Ролл филадельфия",
     "Стейки": "Стейки свинные",
}
n=input("Введите продукт:")
if n in a.keys():
    print(f"{n} есть в холодильнике")
else:
    print(f"{n} нету в холодильнике")
print("\n")

#9
a={
   "Киев": "Украина, согласно легенде, Киев был назван в честь Кия – одного из трех братьев, основавших город, население: 2,884 миллиона",
   "Харьков": "Украина, Три нобелевских лауреата жили в Харькове, население: 1,419 миллиона"
}
for i in a:
    print(i, a[i], "\n")
