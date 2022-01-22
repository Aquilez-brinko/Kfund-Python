#Task1
names = ['Egor', 'Dima', 'Timur']
print(names[-1])
print(names[-2])
print(f'{names[-3]}\n')

#Task2
print(f'{names[0].title()}, давай играть?')
print(f'{names[1].title()}, давай играть?')
print(f'{names[2].title()}, давай играть?\n')

#Task3
car = ['Mercedes-Benz', 'BMW', 'Porsche']
for i in car:
    x=(f'Я хотел бы купить {i.title()}\n')
print(x)

#Task4
people = ['Diana', 'Sofia', 'Zhenya']
for i in people:
    print(f'Привет, {i.title()}, хочу пригласить тебя на обед')
print(f'{people[2]} не сможет прийти\n')

#Task5
del people[2]
people.insert(2, 'Anya')
for i in people:
    print(f'Привет, {i.title()}, хочу пригласить тебя на обед')
print('Можно позвать еще 3 людей\n')

#Task6
people.insert(0, 'Timur')
people.insert(2, 'Egor')
people.append('Yura')
for i in people:
    print(f'Привет, {i.title()}, хочу пригласить тебя на обед')

