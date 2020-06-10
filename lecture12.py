# Functions
"{}년 {}월 {}일 {}요일".format(2020, 2, 2, "월") #'2020년 2월 2일 월요일'

"Hello".upper()
"Hello".lower()
"      String    ".strip()  #공백 제거
"      String    ".lstrip()  #왼쪽 공백만 제거
"      String    ".rstrip()  #오른쪽 공백만 제거

"abcdefg".find("c") #return 2 -> 왼쪽부터 검색 시작
"abcdefg".find("h") #return -1 -> 없는 것을 찾을 때는 -1을 출력한다. 
"abcdefg".rfind("b") #return 1 -> 아이템이 하나만 있을 때는 왼쪽부터 검색
"abcdefgabc".rfind("b") #return 8 -> 가장 오른쪽에 있는 아이템 찾아서 몇 번째인지 출력

"a" in "abcde" #return True
"f" in "abcde" #return False

"10 20 30 40 50".split(" ") #return ['10', '20', '30', '40', '50']

#예제
a = input("> 1st number: ")
b = input("> 2nd number: ")
print()

print("{} + {} = {}".format(a, b, int(a) + int(b)))