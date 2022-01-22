#1
while True:
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    message = input("Вам не надоело ? ")
    if message == "out":
        break
    print(f"Привет {name} {surname}\n")

#2
for i in range(2,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print("-"*12)

