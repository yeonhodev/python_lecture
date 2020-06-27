i = 0

while True:
    print("{}번째 반복문입니다.".format(i))
    i += 1

    input_text = input("> 종료하시겠습니까?(y)")
    if input_text in ["Y", "y"]:
        print("반복을 종료합니다.")
        break

numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
    if number < 10:
        continue #현재 반복을 중지하고, 다음 반복으로 넘어간다. # Continue 키워드를 사용하므로써 드려 쓰기를 줄여 파이썬에서 코드 읽기가 편해지는 경우가 있음.
    print(number)

# Continue 사용 안하고 같은 결과가 가능 1
for number in numbers:
    if number >= 10:
        print(number)

# Continue 사용 안하고 같은 결과가 가능 2
for number in numbers:
    if number < 10:
        pass
    else:
        print(number)

