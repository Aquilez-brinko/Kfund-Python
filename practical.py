#1
names = ['Artem', 'Misha', 'Diana']
for i in names:
    print(f'Привет {i.title()}')
print('\n')

#2
cars = ['BMW', 'Mercedes-Benz', 'Ferrari']
for i in cars:
    x=(f'Я хотел бы купить {i.title()}')
print(f'{x} \n')

#3
years_list = ['2006', '2007', '2008', '2009', '2010', '2011']
print(f'В {years_list[3]} мне было 3 года')
years_list.append('2022')
print(f'В {years_list[6]} мне больше всего лет \n')

#4
things = ['wallet', 'mirror', 'umbrella']
print(things[2].title())
print(things)
print(things[2].upper())
print(things)
del things[2]
print(things)
print('\n')

#5
languages = ['Georgian', 'Estonian', 'Ukrainian']
print(languages[-1].lower())
languages.reverse()
print(f'{languages[0].title()}\n')


#6
hardware = ('mouse', 'keyboard', 'headphones')
software = ['provider', 'router', 'ethernet']
print(hardware)
print(software)
#hardware.append('monitor') - невозможно
software.append('web')

print(f'{software}\n')

#7
languages = ['Vietnamese', 'Ukrainian', 'Spanish', 'Russian']
print(languages)
print(sorted(languages))
languages.reverse()
print(languages)
languages.sort()
print(f'{languages}\n')


#8
numbers = [2, -1, 9, 6]
x = 0
for i in numbers:
    x = x + i 
print(f'{x}\n')

#9
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(i)
print('\n')

#10
List = [2006]
a = List[0]
x = 1
while(a != 2022):
    a = a + x
    List.append(a)
print(List)


