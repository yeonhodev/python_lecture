# finally 구문
try:
  # 예외가 발생할 가능성이 있는 코드
  number = int(input(">정수 입력"))
  print("입력 값은 {}입니다.".format(number))
except:
  # 예외가 발생했을 경우 실행할 코드
  print("예외가 발생했습니다.")
finally: 
  # 옵션[필요에 따라서 사용]
  # 무조건 적으로 실행하는 코드
  print("무조건 적으로 실행됩니다.")

#finally 구문은 사용할 필요가 없는 경우가 많은데, 함수내부에서 return 키워드를 사용하거나, 반복문 내부에서 break 키워드를 사용할 때 의미를 갖는다. -> return 키워드를 만나도 finally 구문은 실행 된다. 

#test() 함수를 선언합니다. 
def test():
  print("test() 함수의 첫 줄입니다.")
  try:
    print("try 구문이 실행되었습니다.")
    return
    print("try 구분의 return 키워드 뒤입니다.")
  except:
    print("except 구문이 실행되었습니다.")
  finally:
    print("finally 구문이 실행되었습니다.")
  print("test() 함수의 마지막 줄입니다.")
#test() 함수를 호출합니다.
test()  

# while 구문과 break 안의 finally 구문
while True:
  print("test() 함수의 첫 줄입니다.")
  try:
    print("try 구문이 실행되었습니다.")
    ㅇㅂㅇ()
    break
    print("try 구분의 return 키워드 뒤입니다.")
  except:
    print("except 구문이 실행되었습니다.")
    break
  finally:
    print("finally 구문이 실행되었습니다.")
  print("test() 함수의 마지막 줄입니다.") 

# finally 구분을 사용하는 예 -> 파일을 열어 사용하고 난 후 반듯이 닫아 주고 싶을 때
# 함수를 선언합니다.
def write_text_file(filename, text):
  # try except 구문을 사용합니다.
  try:
    # 파일을 엽니다.
    file = open(filename, "w")
    # 여러가지 처리를 수행합니다.
    return
    # 파일에 텍스트를 입력합니다. 
    file.write(text)
  except Exception as e:
    print(e)
  finally:
    # 파일을 닫습니다.
    file.close()
# 함수를 호출합니다.
write_text_file("test.txt", "안녕하세요!")