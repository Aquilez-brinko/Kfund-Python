#1
a = 10
i = 0
while a <= 20:
    a=a*1.1
    i+=1
    print(f"Количество дней {i}, Количество км {a}")
print(f"Больше 20 км он пробежит на {i} день\n")
#2
x=1
while x <= 10:
    y=x**2
    print(f"{x} --> {y}\n")
    x += 1
#3
s = 0 
x = 1
print("S = 1 + 2 + 3 + 4 + 5 +.... + n")
n = int(input("n: "))
while x <= n:
    s += x
    x += 1
print(f"Sum of {s} value {x - 1}\n")

#4
e = 1
f = 1
k = int(input("k: "))
while f<=k:
    e *= f
    f+=1
print(f"k! = {e}")



