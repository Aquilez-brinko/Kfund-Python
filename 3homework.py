a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
if(a % b == 0):
    print("Yes")
else:
    print("No")



import math
x = 5
e = 2
c = x - e**x
d = math.log10(x**2)
e = math.sin(x)**2
if(abs(c) < 2 and d <= -2 and x >= 2):
    print("True")
else:
    print("False")
