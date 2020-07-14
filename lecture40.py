#제너레이터
"""
간단하게 "이터레이터를 직접 만들 때 사용하는 구문"
함수 내부에 yield(양보하다, 먼저 가게하다)라는 키워드가 포함되면 해당 함수는 제너레이터가 됩니다. 
"""

def 함수():
  print("출력A")
  print("출력B")

함수()

#yield라는 키워드를 사용하게 되면 아무것도 출력이 되지 않는다. yield라는 키워드가 함수 내부에서 사용되는 순간 그 함수는 제너레이터 함수가 되어서 기본적으로는 실행이 되질 않는다. 
def 함수2():
  print("출력A")
  print("출력B")
  yield

함수2()

#제너레이터 함수는 호출했을 때 제너레이터라는 객체를 리턴한다. 이 제너레이터를 출력해 보면, 제너레이터라는 오브젝트라는 출력이 나옴
def 함수3():
  print("출력A")
  print("출력B")
  yield

제너레이터 = 함수3()
print(제너레이터)

#이를 실행하고 싶으면 next()라는 함수를 사용한다.
next(제너레이터)

# yield 키워드로 return 처럼 값 전달하기
def 함수4():
  print("출력A")
  print("출력B")
  yield 100

제너레이터2 = 함수4()
값 = next(제너레이터2)
print(값)

#yield를 여러개 사용하는 것도 가능 -> 아래의 코드에서는 yield가 하나만 실행 되고 멈춤
def 함수5():
  print("출력1")
  yield 100 #멈춤
  print("출력2")
  yield 200
  print("출력3")
  yield 300
  print("출력4")
  yield 400

제너레이터3 = 함수5()
next(제너레이터3)

#yield가 여러개인 함수에서 출력을 여러개 하려면 next()함수를 여러개 사용해 주면 된다.  
def 함수6():
  print("출력5")
  yield 100 #멈춤
  print("출력6")
  yield 200
  print("출력7")
  yield 300
  print("출력8")
  yield 400

제너레이터4 = 함수6()
next(제너레이터4)
next(제너레이터4)
next(제너레이터4)
next(제너레이터4)

#실제로 제너레이터 함수를 사용할 때는 for문과 사용을 많이 한다. 
def 함수7():
  print("출력9")
  yield 100 #멈춤
  print("출력10")
  yield 200
  print("출력11")
  yield 300
  print("출력12")
  yield 400

제너레이터5 = 함수7()
for i in 제너레이터5:
  print(i)
#for 문을 한번 더 사용해도 두번 출력 되지 않는다. -> 제너레이터 함수는 일회용 함수임
#제너레이터는 이터레이터이므로 reversed()함수와 비슷함
for i in 제너레이터5:
  print(i)

#reversed 함수 복습 -> 일회용 -> 메모리를 절약할 수 있다
numbers = [1, 2, 3, 4, 5]
print(reversed(numbers))
이터레이터 = reversed(numbers)
for i in 이터레이터:
  print(i)
#for반복문을 두번 돌려도 두번 출력 되지 않음
for i in 이터레이터:
  print(i)