#콜백함수; 함수를 매개변수로 받는 함수
def call_10_times(func):
  for i in range(10):
    #콜백함수(callback)
    func()

def print_hello():
  print("안녕하세요")

call_10_times(print_hello)

print()

#함수를 전달 할 때 매개변수로 i를 전달하는 방법
def call_10_times2(func):
  for i in range(10):
    #콜백함수(callback)
    func(i)

#number 안으로 i가 전달 되게 됨
def print_hello2(number):
  print("안녕하세요", number)

call_10_times2(print_hello2)

print()

#람다를 활용해 짧은 형태로 함수를 간단히 정의할 수 있음
def call_10_times3(func):
  for i in range(10):
    func(i)
# :뒤 expression 부분이 return 키워드를 붙인 효과가 나타남
call_10_times3(lambda number: print("안녕하세요", number))

print()

#lambda를 활용하는 함수 filter()와 map()함수
def 짝수만(number):
  return number % 2 == 0

a = list(range(100))
print(a)
b = filter(짝수만, a)
#객체만 출력되므로
print(b)
#리스트로 강제 변환하여 출력해 주거나
print(list(b))
#for 문을 활용해 하나씩 출력도 가능
for i in b:
  print(i)

print()

#람다를 활용하면
c = list(range(100))
d = filter(lambda number: number % 2 == 0 , c)
print(list(d))

print()

#map()함수 - 어떠한 리스트를 기반으로 새로운 리스트를 만들어 주는 함수
def 제곱(number):
  return number * number

e = list(range(100))
print(list(map(제곱, e)))

print()

#람다를 활용해서 짧게 줄이면
f = list(range(100))
print(list(map(lambda number: number * number , f)))

print()

#람다를 리스트 내포와 비교해 보기
print([i * i for i in f])

#if 구문을 더해서 짝수만 출력하게 하면 filter()함수와 map()함수를 동시에 적용한 것과 같은 효과를 내는 것도 가능
print([i * i for i in f if i % 2 == 0])

#람다를 사용하는 것과 리스트내포를 사용하는 것의 차이
#리스트내포를 사용하게 되면 결과로 리스트가 나와 그만큼의 하나가 더 복제되어 메모리를 차지하게 된다.
#filter(), map()함수 등은 제너레이터 함수라서 내부의 데이터가 실제로 메모리에 용창을 차지 하지 않음 -> 제너레이터 함수는 이후에 배움
#최근에는 컴퓨터가 워낙 빨라서 리스트내포를 더 많이 사용하는 추세임