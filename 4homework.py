#1
import math
x = int(input("Введите радиус круга: "))
print(f"Площадь окружности с радиусом {x}: ", math.pi * (x**2))
print(f"Длинна окружности с радиусом {x}: ", 2*math.pi*x, '\n')

#2
x = int(input("Введите пароль: "))
a = 1234
while(x != a):
    print("Пароль неправильный!")
    x = int(input("Введите пароль: "))
else:
    print("Успешно!", '\n')

#3
x = str(input("Здравсвуйте, для взятия кредита необходимо иметь паспорт и достичь 18 лет \nВам есть 18 и паспорт при себе? "))
if(x == "Да"):
    print("Хорошо, держите бланк для заполнения\n")
else:
    print("К сожалению вы не можете взять кредит в нашем банке\n")

#4
x = 7
a = 10
l = [x, a]
y = len(l)
print("Семестр ученика будет - ", round((x + a) / y), '\n')

#5
x = 2
y = 3
if(x > y):
    print(sqrt(x * y, '\n'))
else:
    print(math.log(x+y), '\n')
    
#6
x = int(input("Введите температуру в комнате: "))
if(x>20):
    print("on\n")
else:
    print("off\n")

#7
x = int(input("Каким по счету стоит Вася? "))
if(x % 2 == 0):
    print("Вторым\n")
else:
    print("Первым\n")

#8
a = int(input("Введите 1-ю сторону треугольника "))
b = int(input("Введите 2-ю сторону треугольника "))
c = int(input("Введите 3-ю сторону треугольника "))
if(a + b >= c and a + c >= b and b + c >= a):
    if(c**2 == a**2 + b**2 or b**2 == c**2 + a**2 or a**2 == c**2 + b**2):
        print("Существует, прямоугольный\n")
    elif(c**2 < a**2 + b**2 or b**2 < a**2 + c**2 or a**2 < c**2 + b**2):
        print("Существует, остроугольный\n")
    elif(c**2 > a**2 + b**2 or b**2 > a**2 + c**2 or a**2 > c**2 + b**2):
        print("Сущесвтует, тупоугольный\n")
    else:
        print("Не существует\n")

#9
x = int(input("Координата x: "))
y = int(input("Координата y: "))
if(x > 0 and y > 0):
    print("I\n")
elif(x < 0 and y > 0):
    print("II\n")
elif(x < 0 and y < 0):
    print("III\n")
elif(x > 0 and y < 0):
    print("IV\n")

#10
x = int(input("Введите x: "))
if(x > 0):
    y = 2*x-10
    print(y, '\n')
elif(x == 0):
    y = 0
    print(y, '\n')
else:
    y = 2*abs(x)-1
    print(y, '\n')
