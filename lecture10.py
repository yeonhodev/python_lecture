pi = 3.14
print(pi)

pi = pi + 3.14
print(pi)

pi += 10
print(pi)
pi -= 10
print(pi)

a = input(">>> ")
print(a)
print(type(a)) #input의 output은 무조건 Str 이므로 숫자를 입력해도 문자열로 반환 됨
#print(input(">>> "))

b = input("Choose first number> ") # Type 100
c = input("Choose second number> ") # Type 200
print(b + c) # Result -> 100200