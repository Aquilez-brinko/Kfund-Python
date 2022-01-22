animal=['frog', 'horse', 'bear']
a= f'Это {animal[1].upper()}'
b= f'Это {animal[1].title()}'
print(a)
print(b)
animal[2]='bat'
print(animal[2])
animal.append('mouse')
print(animal[3])
animal.insert(2,'cat')
print(animal[2])


user = ['u1', 'u2', 'u3', 'u4']

user_V = []
print(user)
while user:
    u = user.pop(0)
    user_V.append(u)
    print(f"Пользователи прошли вeрификацию {u.title()}")
print(user)
print(f"Пользователи прошли вeрификацию {user_V}")

for i in animal:
    text = f'Я хочу {i.title()}'
    print(text)
print(animal)
