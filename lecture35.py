#재귀함수와 메모화

# n! = 1 * 2 * 3 * ... (n-2) * (n-1) * n
def factorial_1(n):
    변수 = 1
    for i in range(1, n + 1):
        변수 *= i
    return 변수

# n! = n * (n - 1)!
# 0! = 1
# 함수 내부에서 함수를 호출 하는 함수를 재귀함수라고 한다.
def factorial_2(n):
    if n == 0:
        return 1
    else:
        return n * factorial_2(n - 1)

print(factorial_1(10))
print(factorial_2(10))

#피보나치 수열
# f(1) = 1
# f(2) = 1
# f(n) = f(n-1) + f(n-2)
def f(n):
    if n == 1 or n == 2:
        return 1
    else: 
        return f(n - 1) + f(n - 2)

print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))

#재귀함수를 아래와 같이 구현할 때는 반복 계산이 많아져 불필요하게 계산 횟수가 많아져 속도가 느려진다.
counter = 0
def f(n):
    global counter
    counter += 1
    if n == 1 or n == 2:
        return 1
    else: 
        return f(n - 1) + f(n - 2)
print(f(35))
print(counter)

#메모화 (memoization)
메모 = { 1: 1, 2: 1}
def f(n):
    if n in 메모:
        return 메모[n]
    else:
        output = f(n-1) + f(n -2)
        메모[n] = output
        return output
print(f(150))

#조기리턴을 활용해 else 부분을 제거하고 들여쓰기 단계를 줄여주면 더욱 좋은 코드가 된다. -> 아래 코드도 결국 위와 같이 작동 함. 
메모2 = { 1: 1, 2: 1}
def f(n):
    if n in 메모2:
        return 메모2[n]
    output = f(n-1) + f(n -2)
    메모2[n] = output
    return output
print(f(150))