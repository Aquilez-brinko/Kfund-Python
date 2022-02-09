# user = {
#     "u1": "Человек",
#     "u2": "Супергерой",
#     "u3": "Броколли",
#     "u4": "Волк"
# }
# print(user)
# print(user["u3"])
# user["u5"] = "Programmer"
# print(user)

# user = {}

# user["u1"] = "Человек",
# user["u2"] = "Супергерой",
# user["u3"] = "Броколли"
# print(user)

# user["u2"] = "Волк"
# print(user)


# info = {"x": 10, "y": 30, "player_speed": "medium"}
# if info["player_speed"] == "medium":
#     x_increment = 2
# elif info["player_speed"] == "fastest":
#     x_increment = 10
# else:
#     x_increment = 1
# info["x"] += x_increment
# print(f"Новая позиция игрока: {info['x']}")

# language = {
#     "aleksey":"python",
#     "ilya":"c++",
#     "xlebich":"js",
#     "vanya":"python(crutoy)",
#     "nikiton":"php"
#     }
# print(f"Я люблю программировать на {language['ilya'].title()} языке программирования")
# for i, g in language.items():
#     print(f"Меня зовут {i.title()}.Я люблю программировать на {g} языке программирования")
# for x in language.keys():
#     print(f"Меня зовут {x.title()}.")
# for t in language.values():
#      print(f"Меня зовут {x.title()}.")



# info1 = {
#     "color1":"red",
#     "points": 5
# }
# info2 = {
#     "color1":"yellow",
#     "points": 15
# }
# info3 = {
#     "color1":"green",
#     "points": 25
# }

# list_1 = [info1,info2,info3]

# for i in list_1:
#     print(i)

list_huge = []
for i in range (30):
    info = {
        "color1":"yellow",
        "points": 15
    }
    list_huge.append(info)
    print(f"{list_huge}")
for p in list_huge[0:3]:
    if p["color1"] == "yellow":
        p["color1"] = "blue"
        p["points"] = 100
for x in list_huge:
    print(x)
print(f"кол-во игроков {len(list_huge)}")
