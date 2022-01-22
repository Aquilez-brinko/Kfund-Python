#1
print(f'Сумма чисел = {2 + 7 + 21 + 9 + 33 + 13}\n')

#2
a = 7
x = 7
while(a != 25):
    a += 2
    x = x + a
print(f'Сумма непарных чисел от 7 до 25 = {x}\n')

#3
i=1
x=1
while(x <= 5):
    i += 1
    x = x + i
print(f'Сумма чисел натурального ряда не больше 7 = {x}\n')

#4
a=6
b=0.5
i=1
x=0
while(a*b >= 0.6):
    print(f'b{i} = {a*b}')
    x = x + a*b
    i += 1
    b = 0.5**i
print(f'Последний номер прогресии = {i-1}, сумма прогресии = {x}\n')

#5
i = 4
x = 3
while(i != 0):
    print(f'Обэм куба{i+1} = {x**3}')
    x += 1.5
    i -= 1
print(f'Обэм куба{i+1} = {x**3}\n')

#6
import math
i=6
r=2
l=0.5
x=0
while(i != 0):
    x= 4*math.pi*r**2
    r += l
    i -= 1
    print(f'Площадь боковых поверхностей шара = {x}')
print('\n')

#7
class1 = [120, 20, 50, 20, 88]
class2 = [133, 21, 33, 21, 92]
class3 = [15, 33, 30, 11, 43]
print(f'Среднее время проплыва первого класса = {sum(class1) / len(class1)}')
print(f'Среднее время проплыва первого класса = {sum(class2) / len(class2)}')
print(f'Среднее время проплыва первого класса = {sum(class3) / len(class3)}')

#8
s = int(input('Какую сумма вы хотите внести? '))
n = int(input(f'Под какой процент вы хотите внести {s} грн? '))
i = 0
while(n+1 > i):
    p = s/100*n
    s += p
    i += 1
    print(s)
print('\n')

#9
a=int(input('Введите число: '))
b=int(input('Введите число: '))
c=int(input('Введите число: '))
if(a>b>c):
    print(f'{a*2}, {b*2}, {c*2}\n')
else:
    print(f'{a-1}, {b-1}, {c-1}\n')

#10
a=int(input('Введите 1 сторону: '))
b=int(input('Введите 2 сторону: '))
c=int(input('Введите 3 сторону: '))
if(a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2):
    print('Прямоугольный\n')
else:
    print('Не прямоугольный\n')

#11
v=5
h=3
a=int(input('Введите скорость ветра на сегодня в Киеве: '))
b=int(input('Введите облачность в Мюнхене: '))
if(a<v and b>=h):
    print('Самолет вылетет вовремя\n')
else:
    print('Самолет не вылетет вовремя\n')

#12
a=int(input('Введите очки 1 школьника: '))
b=int(input('Введите очки 2 школьника: '))
c=int(input('Введите очки 3 школьника: '))
if(a>=5 and b>=5 and c>=5):
    print('Школьники пройдут в финал\n')
else:
    print('Школьники не пройдут в финал\n')

#13
x=100
a=int(input('Введите очки 1 участника: '))
b=int(input('Введите очки 2 участника: '))
if(a>=100 and b>=100):
    print('Оба участники прошли\n')
elif(a>=100 and b<100):
    print('Прошел только первый участник\n')
elif(a<100 and b>=100):
    print('Прошел только воторой участник\n')
elif(a<100 and b<100):
    print('Оба участники не прошли\n')

#14
import random
a=random.randint(0,3)
b=random.randint(0,3)
c=random.randint(0,3)
d=random.randint(0,3)
print(f'Динамо-{a}, Ворскла-{b}')
print(f'Шахтар-{c}, Днiпро-{d}')
if(a>b and c<d):
    print('Динамо чемпион!')
elif((a>b and c>d) or (a<b and c<d)):
    print('Динамо не станет чемпионом')
elif(a==b or c==d or d==c or b==a):
    print('Динамо не станет чемпионом')
