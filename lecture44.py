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
  #print(type(exception))
  #print(exception)
  if type(exception) == ValueError:
    print("값에 문제가 있습니다.")


# if 조건문으로 예외 구분하기
try:
  a = [273, 103, 52, 57, 100]
  number = int(input("정수 입력(0~4까지 입력 해 주세요.)> "))
  print(a[number])
except Exception as exception:
  print(type(exception))
  if type(exception) == ValueError:
    print("값에 문제가 있습니다.")
  elif type(exception) == IndexError:
    print("0~4까지 입력 해 주세요.")

#들여쓰기를 사용하지 않고 윗쪽의 코드를 똑같이 구현하는 방법
try:
  a = [273, 103, 52, 57, 100]
  number = int(input("정수 입력(0~4까지 입력 해 주세요.)> "))
  print(a[number])
except ValueError as exception:
  print("값에 문제가 있습니다.")
except IndexError as exception:
  print("0~4까지 입력 해 주세요.")
except Exception as exception: #마지막에는 오류가 나더라도 꼭 걸릴 수 있게 Exception을 무조건 사용해 주는 것이 좋다. 
  print("알 수 없는 예외가 발생했습니다.")
  #개발자에게 메일을 보낸다. 


# raise 예외객체 -> 개발자를 위한 라이브러리를 개발할 때 주로 사용한다.
raise Exception("안녕하세요.")