#가변 매개변수와 기본 매개변수 (variable parameters and default parameters)
# 매개변수는 함수의 안에 들어가는 변수
# - 보통 매개변수의 갯수는 정해져 있는데, print()함수와 같이 안에 매개변수의 갯수와 상관 없이 실행되는 것을 가변 매개변수라고 함

def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요", 5)

#가변매개변수 만들어 보기
# - 가변매개변수는 함수 안 가장 마지막에 하나만 들어갈 수 있다.
# - 가변매개변수를 직접 만들 일은 거의 없지만, 가변매개변수가 들어있는 함수를 이해 할 수 있어야 한다. 
def 함수이름(매개변수1, 매개변수2, *가변매개변수):
    print(매개변수1)
    print(매개변수2)
    print(가변매개변수)

함수이름(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

#기본 매개함수 만들어 보기
#매개변수 뒤에 default 값을 정해줄 때 아래와 같이 "=값"을 입력 해 주면 됨
#기본 매개변수가 설정된 매개변수는 가장 마지막에 위치 해야 함
def print_n_times(value, n=3):
    for i in range(n):
        print(value)

print_n_times("안녕하세요")