print(min([273, 52, 32, 57, 103]))
print(max([273, 52, 32, 57, 103]))
print(min(273, 52, 32, 57, 103))
print(max(273, 52, 32, 57, 103))
print(sum([273, 52, 32, 57, 103]))

a = [0, 1, 2, 3, 4, 5]
reversed_a = reversed(a)
for i in reversed_a:
    print(i, end=" ")
print()

for i in reversed_a:
    print(i, end=" ") # reversed_a 가 일회용 함수라 한번만 출력 됨
print()

# reversed 함수를 두번 모두 출력하고 싶으면 아래와 같이 사용하고자 하는 함수를 for 구문 안에 직접 써야 함
b = [0, 1, 2, 3, 4, 5]
for i in reversed(a):
    print(i, end=" ")
print()

for i in reversed(a):
    print(i, end=" ") # reversed_a 가 일회용 함수라 한번만 출력 됨
print()

#enumberate 함수 -> enumerate함수도 또한 일회용 함수이다. 
c = [273, 52, 32, 57, 103]
print(list(enumerate(c)))

d = [273, 52, 32, 57, 103]
for i, element in enumerate(d):
    print("{}번째 요소는 {} 입니다.".format(i, element))

#items 함수
e = {"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}
for key, value in e.items():
    print("{}키의 값은 {}입니다.".format(key, value))

# 위의 내용 요약정리
min(리스트) or min(숫자, 숫자, 숫자, ...)
max(리스트) or max(숫자, 숫자, 숫자, ...)
sum(리스트)
for i in reversed(리스트):
for i, element in enumerate(리스트):
for key, value in 딕셔너리.items():