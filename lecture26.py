i = 0
while i < 10:
    print(i, end=" ")
    i += 1

numbers = [1, 2, 1, 2, 1, 2, 1, 2]
numbers.remove(1)
print(numbers) #첫번째 1 하나만 삭제가 됨

numbers2 = [1, 2, 1, 2, 1, 2, 1, 2]

while 1 in numbers2:
    numbers2.remove(1) #반복을 통해 모든 1을 제거하게 됨
    print(numbers2) 

#5초 동안 대기하는 프로그램 만들기
import time
처음 = time.time()
while 처음 + 5 >= time.time():
    pass
print("프로그램이 종료되었습니다.")