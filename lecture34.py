# return -> 너가 왔던 곳으로 다시 돌아가!

def function():
    print("A")
    print("B")
    return 100

print(function())

print()

def function2():
    print("A")
    print("B")
    return #??

print(function2())

#함수의 기본 구조
def 함수(매개변수):
    변수 = 초깃값
    #여러 가지 처리
    #여러 가지 처리
    #여러 가지 처리
    return 변수

# start ~ end 까지 있는 모든 정수를 더하는 함수
def sum_all(start, end):
    변수 = 0
    for i in range(start, end + 1):
        변수 += i
    return 변수

print(sum_all(1, 100))
print(sum_all(50, 100))

def f_1(x):
    return (2 * x) + 1

print(f_1(10))

def f_2(x):
    return (x ** 2) + (2 * x) + 1

print(f_2(10))

#매개변수로 전달 된 값들을 모두 곱해서 리턴하는 가변 매개변수 함수를 만들어 보세요. 
def mul(*values):
    변수 = 1
    for i in values:
        변수 *= i
    return 변수
print(mul(5, 7, 9, 10))