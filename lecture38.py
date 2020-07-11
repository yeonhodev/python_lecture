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

call_10_times3(lambda number: print("안녕하세요", number))