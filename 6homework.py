#1
a = 10
i = 0
b = 0
for i in range (0,8,1):
    a=a*1.1
    i = i + 1
    print(f"Количество дней {i}, Количество км {a}")
print(f"Больше 20 км он пробежит на {i} день\n")

#2
x=1
for x in range(0,11,1):
    y=x**2
    print(f"{x} --> {y}\n")
    
#3
s = 0 
x = 1
a = 0
c = x
print("S = 1 + 2 + 3 + 4 + 5 +.... + n")
n = int(input("n: "))
for x in range(0,n+1,1):
    s += x
    
    a = a + 1
print(f"Sum of {s} value {a-1}\n")

#4
e = 1
f = 1
k = int(input("k: "))
for f in range(1,k+1,1):
    e = e * f
print(f"k! = {e}")

#5
a = 1
s = 0
x = int(input("x: "))
for a in range(1,x+1,2):
    s = s + a
print(f"S={s}\n")

#6
x = int(input("x: "))
s = 0
a = 2
i = 0
for i in range(0,x,1):
    s = s + 1/a
    a = a * 2
print(f"S={s}\n")

#7
i = 0
x = int(input("x: "))
while x > 0:
    x //= 10
    i += 1
print(f"Количесвто цыфр в числе = {i}")
