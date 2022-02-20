#1
def message(i):
    print(f"Привет {i}\n")
name=input("Введите имя: ")
message(name)

#2
def func(t, r):
    return t
item = input("Введите текст: ")
n = int(input("Количество текста: "))
a = func(item, n)
for i in range (n):
    print(a)
print("\n")

#3
def func(num1,num2):
    if num1 > num2:
        z = f"{num1} > {num2}"
    elif num2 > num1:
        z = f"{num2} > {num1}"
    else:
        z = "equal"
    return z
num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))
y = func(num1,num2)
print(y)
print("\n")

#4
def func(num1,num2,num3):
        z = max(num1,num2,num3)
        return z
num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))
num3 = int(input("Третье число: "))
y = func(num1,num2,num3)
print(f"Наибольшое число {y}\n")


#5
def func(num1,num2,num3):
    if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
        z = "Треугольник существует\n"
    else:
        z = "Треугольник не существует!\n"
    return z
num1 = int(input("Первая сторона: "))
num2 = int(input("Вторая сторона: "))
num3 = int(input("Третья сторона: "))
y = func(num1,num2,num3)
print(y)

#6
def func(word1,word2):
    z = word1 + "" + word2
    return z
word1 = input("Первое слово: ")
word2 = input("Второе слово: ")
y = func(word1,word2)
print(f"{y}\n")

#7
def func(op1,op2,op3,x,i=1):
    if op3 == "+": 
        x = op1 + op2
    elif op3 == "-": 
        x = op1 - op2
    elif op3 == "*": 
        x = op1 * op2
    elif op3 == "/": 
        x = op1 / op2
    else:
        x = "Unknown operation"
        return x
    return f"{x:.{i}f}"
op1 = int(input("Первое число: "))
op2 = int(input("Второе число: "))
op3 = (input("Операция (+, -, *, /): "))
x = 0
y = func(op1,op2,op3,x,2)
print(f"{y}\n")

#8
def func(tag,text):
    z = f"<{tag}>{text}<{tag}>\n"
    return z
tag = input("Тэг: ")
text = input("Текст: ")
y = func(tag,text)
print(y)

#9
def func(x):
    if x<=2 or x==12:
        m = "Winter\n"
    elif x>2 and x <=5:
        m = "Spring\n"
    elif x>5 and x <=8:
        m = "Summer\n"
    elif x>8 and x <=11:
        m = "Autumn\n"
    else:
        m = "Месяц не найден\n"
    return m
x = int(input("Номер месяца: "))
y = func(x)
print(y)

#10
def func(n):
    for i in n:
        print("*" * i)
func([2,7,1,4,2,3,9,3] )
print("\n")

#11
def num(a):
    if a % 2 == 0:
        print("Число парное\n")
    else:
        print("Число непарное\n")
a = int(input("Введите число: "))
num(a)

#12
def func(numbers):
    x = [numbers[0], numbers[-1]]
    print(x)
numbers = [5, 16, 72, 29, 11, 217, 112]
func(numbers)
print("\n")

#13
def fact(x, i = a, z = a) :
    while i <= x:
        i *= z
        z += a
    print(i)
x = int(input("Введите факториал: "))
fact(x)
print("\n")

#14
import math
def triangle(side1, side2, side3):
    p = (side1 + side2 + side3)/2
    print(math.sqrt(p*(p-side1)*(p-side2)*(p-side3)))
          
def check_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False
def circle(r):
    print(math.pi * math.pow(r, 2))
def rectangle(a, b):
    print(a*b)
def check_the_figure(name):
    if name == "треугольник" :
        side1 = int(input("1 сторона: "))
        side2 = int(input("2 сторона: "))
        side3 = int(input("3 сторона: "))
        if check_triangle(side1, side2, side3): 
            triangle(side1, side2, side3)
        else :
            print("Треугольник не может существовать")
    elif name == "круг" :
        r = int(input("Радиус круга: "))
        circle(r)
    elif name == "прямоугольник" :
        a = int(input("1 сторона прямоугольника: "))
        b = int(input("2 сторона прямоугольника: "))
        rectangle(a, b)
check_the_figure(input("Введите название фигуры(треугольник,круг,прямоугольник): "))
