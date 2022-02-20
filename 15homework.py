#1
def city_country(city, country):
     return f"{city}, {country}"
print(city_country("Ukraine", "Kiev"))
print(city_country("Russia", "Moskow"))
print(city_country("USA", "New York\n"))

#2
i=0
music_album1= {}
def make_album(name):
    info = f"{name}"
    return info

while i!=3:
    print("Если хочешь прекратить, то введи stop")    
    n = input("Исполнитель? ")
    i=i+1
    if n == "stop":
        break
    s = input("Альбом? ")
    music_album1[f"{n}"]=f"{s}"
    y = make_album(music_album1)
    print(y)

