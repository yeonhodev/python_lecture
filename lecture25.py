#range(시작, 끝, 단계)
#range(시작, 끝) -> 단계=1 생략
#range(끝) -> 시작=0과 단계=1 생략
range(0, 10, 1) # 0부터 10까지 1씩 증가한다

list(range(0, 10, 1)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(0, 10, 2)) # [0, 2, 4, 6, 8]
list(range(0, 10, 3)) # [0, 3, 6, 9]
list(range(0, 10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(10, 0, -1)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(0, 10, 1):
    print(i)

#for 반복문에서 element가 몇 번째 인지 아는 방법 1
array = [273, 52, 103, 32, 57]
i = 0

for element in array:
    print("{} : {}".format(i, element))
    i += 1

#for 반복문에서 element가 몇 번째 인지 아는 방법 2
array = [273, 52, 103, 32, 57]

for i, element in enumerate(array):
    print("{} : {}".format(i, element))

#for 반복문에서 element가 몇 번째 인지 아는 방법 3
array = [273, 52, 103, 32, 57]

for i in range(len((array))):
    print("{} : {}".format(i, array[i]))

#역 반복문 방법 1
for i in range(9, -1, -1):
    print(i)

#역 반복문 방법 1
for i in reversed(range(10)):
    print(i)

for i in reversed(array):
    print(i)