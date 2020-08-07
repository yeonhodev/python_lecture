from flask import Flask
app = Flask(__name__)

@app.route("/") # 데코레이터(@으로 시작함) : 어떤 함수에 "미리 만든 규격화된 처리"를 적용할 때 사용하는 것
# 함수 데코레이터: 함수로 만든 데코레이터
# 클래스 데코레이터: 클래스로 만든 데코레이터
def hello():
  return "<h1>Hello World!</h1>"

# 간단한 함수 데코레이터의 예
def 데코레이터(함수):
  print("미리 어떤 처리를 진행합니다.")
  return 함수

def 테스트():
  print("안녕하세요")

테스트 = 데코레이터(테스트)
테스트()

print()

# 위의 코드를 데코레이터를 활용해 똑같이 작성하는 방법
def 데코레이터(함수):
  print("미리 어떤 처리를 진행합니다.")
  return 함수

@데코레이터
def 테스트():
  print("안녕하세요")

테스트()

#매개변수를 전달하는 방법
def 외부데코레이터(number):
  def 데코레이터2(함수):
    print("미리 어떤 처리를 진행합니다.", number)
    return 함수
  return 데코레이터2

@외부데코레이터(number=100)
def 테스트2():
  print("안녕하세요")

테스트2()


# 상속: Inheritance - 어떤 클래스가 갖고 있는 기능을 물려받는 것
# 클래스 > 최상위 부모클래스 무조건 상속!!

class 부모:
  def 테스트(self):
    print("안녕하세요!")

class 자식(부모):
  pass

print(부모.mro())
print(자식.mro())

c = 자식()
c.테스트()
