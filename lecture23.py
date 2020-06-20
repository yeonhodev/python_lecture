list = []
list = [1, 2, 3, 4, 5]
list[0]

#딕셔너리 선언
dictionary = {
    "keyA": "valueA",
    273: [1, 2, 3, 4],
    True: False
}
print(dictionary["keyA"])
print(dictionary[273])
print(dictionary[True])

dictionary["keyA"] = "valuevalue"
print(dictionary["keyA"])

#반복문
for key in dictionary:
    print("{} : {}".format(key, dictionary[key]))

# 요소 추가
dictionary["newkey"] = "newvalue"

for key in dictionary:
    print("{} : {}".format(key, dictionary[key]))

# 요소 제거
del dictionary["newkey"]
print()
for key in dictionary:
    print("{} : {}".format(key, dictionary[key]))