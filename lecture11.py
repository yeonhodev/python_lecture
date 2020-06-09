a = input("Choose first number> ") # Type 100
b = input("Choose second number> ") # Type 200
print(a + b) # Result -> 100200

c = int(input("Choose first number> ")) # Type 100
d = int(input("Choose second number> ")) # Type 200
print(c + d) # Result -> 300
#float을 입력하면 오류 발생하게 됨

e = float(input("Choose first number> ")) # Type 100.0
f = float(input("Choose second number> ")) # Type 200.0
print(e + f) # Result -> 300.0

# Int -> Str
type(str(123)) # Str

# 교체하는 방법
print(a, b)
c = b
b = a
a = c
print(a, b)

# Python에서 간단히 교체 가능한 방법
print(a, b)
a, b = b, a
print(a, b)