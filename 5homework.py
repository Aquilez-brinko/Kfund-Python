#1
a = 1
s = 0
x = int(input("x: "))
while a <= x:
    s = s + a
    a = a + 2
print(f"S={s}\n")

#2
x = int(input("x: "))
s = 0
a = 2
while x > 0:
    s = s + 1/a
    a = a * 2
    x = x - 1
print(f"S={s}\n")

#3
i = 0
x = int(input("x: "))
while x > 0:
    x //= 10
    i += 1
print(f"Количесвто цыфр в числе = {i}")
