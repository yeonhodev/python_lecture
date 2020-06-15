a = [1, 2, 3, 4, 5, 6, 7]

for element in a:
    print(element)

# Print numbers which is the equal or higher than 100.
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number >= 100:
        print(number)

for number in numbers:
    if number % 2 == 0:
        print("{} is an even number.".format(number))
    else:
        print("{} is an odd number.".format(number))

for number in numbers:
    print("{} is a {}-digit number.".format(number, len(str(number))))

list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for list in list_of_list:
    for item in list:
        print(item)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    output[(number - 1) % 3].append(number)
print(output)

# 중요 -> 리스트에서 정수로 요소를 추출하는 방법 그리고 주의사항
b = [1, 2, 3, 4, 5, 6, 7]
b[1] #2
b[1 + 1] #3
b[1 - 1] #1
b[1 * 1] #2
#b[1 / 1] #에러 발생 -> 나누기 연산자는 무조건 소숫점 한자리까지 반환해 "1.0" float가 됨
b[1 // 1] #2 -> 정수 나누기 연산자를 사용해 줘야 함을 꼭 기억!!!

#응용 문제
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

holzzak = ["even", "odd"]
for number in numbers: 
    print("{} is an {}.".format(number, holzzak[number % 2]))