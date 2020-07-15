# 구문 오류(syntax error) - 코드에 문제가 있어서 실행 안됨
"""
print("실행되었습니다.")
print("test)
"""

# 예외(런타임 오류) - 코드 자체에 문법적인 오류는 없지만, 실행과 관련된 문제로 인해 실행은 되지만 죽어버리는 오류
"""
print("실행되었습니다.")
list_a = [1, 2, 3]
print(list_a[100])
"""

#예외가 발생 할 수 있는 코드 -> 정수를 입력하지 않을 경우 에러 발생함
# 숫자를 입력받습니다. 
number_input_a = int(input("정수 입력> "))

# 출력합니다. 
print("원의 반지름:", number_input_a)
print("원의 둘레:", 2 * 3.14 * number_input_a)
print("원의 넓이:", 3.14 * number_input_a * number_input_a)

#정수를 입력하지 않을 경우, 다시 입력을 요청하면 예외 처리가 가능해짐
while True:
  string_input = input("정수 입력> ")
  if string_input.isdigit():
    number_input_b = int(string_input)
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
    break
  
  else: 
    print("정수를 입력해 주세요!")