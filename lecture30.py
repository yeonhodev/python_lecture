# 리스트 내포 (List Comprehension)
array = []
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
for i in range(0, 20, 2):
    # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
    array.append(i * i)

print(array)

array_2 = [i * i for i in range(0, 20, 2)]
print(array_2)

array_3 = [i for i in range(10)]
array_4 = [i for i in range(0, 10, 2)]
array_5 = [1 for i in range(10)]

print(array_3)
print(array_4)
print(array_5)

array_6 = [i for i in range(10) if i % 3 == 0]
print(array_6)

# 1~100 / 2진수 / 0이 하나만 포함된 숫자 > 합!!
output = 0
for i in range(1, 100 + 1):
    # 2진수로 변환 한게 0을 카운트 했을 때 그 수가 1인 경우
    if "{:b}".format(i).count("0") == 1:
    #10진수를 2진수로 변환해서 프린트
        print("{:b}".format(i))
        print("{} : {:b}".format(i, i))
        output += i
print("합계: {}".format(output))

print("----------")

#한줄로 변환
output_2 = [i for i in range(1, 100 + 1) if "{:b}".format(i).count("0") == 1]
print(output_2)
for i in output_2:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계: {}".format(sum(output_2)))