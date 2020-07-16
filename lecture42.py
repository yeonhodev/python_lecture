#try except 구문
while True:
  try:
    #예외가 발생할 수 있는 가능성이 있는 코드
    print(float(input("숫자를 입력해 주세요: ")) ** 2)
    break
  except:
    #예외가 발생했을 때 실행할 코드
    #print("숫자를 입력해 주세요.")
    #아무것도 실행 하고 싶지 않을 때는 아래처럼 "pass" 키워드를 사용해 주면 됨
    pass

#예제
# 변수를 선언합니다. 
list_input_a = ["52", "273", "32", "스파이", "103"]

# 반복문을 적용합니다. 
list_number = []
for item in list_input_a:
  # 숫자로 변환해서 리스트에 추가합니다. 
  try:
    float(item) # 예외가 발생하면 알아서 다음으로 진행은 안 되겠지?
    list_number.append(item) #예외없이 통과했으면 리스트에 넣어줘!
  except:
    pass

#출력합니다.
print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))


#리스트 내부에서 특정 값이 어디 있는지 확인할 때는 리스트의 index() 함수를 사용한다.
# 같은 값이 여러개 있을 때는 왼쪽 부터 가장 처음 있는 것을 리턴 함
numbers = [11, 12, 13, 14, 15]
print(numbers.index(11)) #0
print(numbers.index(14)) #3


#예제 - if 구문을 활용하기
numbers2 = [11, 12, 13, 14, 15]
print("# (2) 요소 내부의 없는 값 찾기")
number = 10000
if number in numbers:
  print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
else:
  print("- 리스트 내부에 없는 값입니다.")
print()

#예제 - try except 구문을 활용하기
numbers2 = [11, 12, 13, 14, 15]
print("# (2) 요소 내부의 없는 값 찾기")
number = 10000
try:
  print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
except:
  print("- 리스트 내부에 없는 값입니다.")
print()