list = []
list = [1, 2, 3, 4, 5]
list[0]

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

for key in dictionary:
    print("{} : {}".format(key, dictionary[key]))

# 새로운 키와 값 추가
dictionary["newkey"] = "newvalue"

for key in dictionary:
    print("{} : {}".format(key, dictionary[key]))

# 값 제거하기
del dictionary["newkey"]
print()
for key in dictionary:
    print("{} : {}".format(key, dictionary[key]))