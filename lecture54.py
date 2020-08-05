# 파일이 여러개로 분할 되게 되면 내가 지금 실행되고 있는 파일이 어떤 부분인지 알아야 할 필요가 있다. 그래서 __name__이라는 특수한 변수가 만들어 졌다. __name__을 사용해서 내가 지금 어떤한 파일에 있는지 확인이 가능하다. 
print(__name__) #Entry point에서는 모듈 이름 대신 "__main__"이라고 출력된다. -> 이를 이용해 현재 실행되고 있는 파일이 엔트리 포인트인지 아래의 코드를 활용해 확인이 가능하다. 
if __name__ == "__main__":
  print("엔트리 포인트입니다.A")
# "python 파일.py" 을 통해 파일을 실행하면 이 파일에서 다른 모듈들을 불러오거나 자신의 코드를 호출하면서 코드를 실행하게 된다. 이때 이 파일을 진입점 (Entry Point or main이라고 부르기도 한다.)
# 파일 > 모듈 > 모듈 > 모듈

#how to create and import a module
import my_module
print(my_module.a)
print(my_module.b)
print(my_module.c())