#정수를 입력하면 제대로 작동하고, 그렇지 않으면 예외가 발생하는 코드
try:
  number_input_a = int(input("정수 입력> "))
  print("원의 반지름:", number_input_a)
  print("원의 둘레:", 2 * 3.14 * number_input_a)
  print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except:
  print("예외가 발생했습니다.")


#예외 객체
try:
  number_input_a = int(input("정수 입력> "))
  print("원의 반지름:", number_input_a)
  print("원의 둘레:", 2 * 3.14 * number_input_a)
  print("원의 넓이:", 3.14 * number_input_a * number_input_a)
#except 예외의종류 as 변수로사용할이름:
#예외의종류에 무엇을 넣을지 모를 때는 모든 예외들의 어머니로 부를 수 있는 Exception을 넣는다 -> Exception 처럼 대문자로 시작하는 것은 Class임
except Exception as exception:
  print(type(exception))
  print(exception)

# 2:30