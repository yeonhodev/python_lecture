dictionary = {
    "name": "cloud", 
    "race": "dog"
}

dictionary["name"] #"cloud"

#Dictionary에 없는 값을 출력하려고 할 경우 Error가 발생하는데, 
# 값이 있는지 없는지 먼저 확인을 해서 에러가 발생하지 않도록 하는 방법
# Dictionary에 key가 있는지 없는지 먼저 확인하는 법
if "age" in dictionary:
    print(dictionary["age"])
else:
    print("The key doesn't exist.")

print(dictionary.get("name"))
print(dictionary["name"])
#get 함수를 사용하면 없는 값에서 에러 대신 None이라는 값을 출력해 줌
print(dictionary.get("age"))

if dictionary.get("age") == None:
    dictionary.get("age")
else:
    print("No key exists")

# 딕셔너리를 선언합니다. 
pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 2},
    {"name": "호랑이", "age": 1}
]

print("# 우리 동네 애완 동물들")
for pet in pets:
    print("{} {}살".format(pet["name"], pet["age"]))

numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3,]
counter = {}

#고정적으로 사용 되는 카운터 함수 이므로 그냥 외우기
for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)

#Flatten
character = {
    "name": "기사",
    "level": "12",
    "item": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill":["베기", "세게 베기", "아주 세게 베기"]
}
# For 반복문을 사용합니다. 
for key in character:
    if type(character[key]) is dict:
        for k in character[key]:
            print("{} : {}".format(k, character[key][k]))
    elif type(character[key]) is list:
        for item in character[key]:
            print("{} : {}".format(key, item))
    else:
        print("{} : {}".format(key, character[key]))
