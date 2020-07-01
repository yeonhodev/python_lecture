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

# 두번 모두 출력하고 싶으면 아래와 같이 사용하고자 하는 함수를 for 구문 안에 직접 써야 함
a = [0, 1, 2, 3, 4, 5]
for i in reversed(a):
    print(i, end=" ")
print()

for i in reversed(a):
    print(i, end=" ") # reversed_a 가 일회용 함수라 한번만 출력 됨