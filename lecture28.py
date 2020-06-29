key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(len(value_list)):
    character[key_list[i]] = value_list[i]

#최종출력
print(character)
# {'name': '기사', 'hp': 200, 'mp': 50, 'level':5}