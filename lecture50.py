import sys

print(sys.version)
print(sys.copyright)

#명령 매개변수 -> 인공지능 개발 시 많이 사용하게 됨 -> "python lecture50.py 0 2 3"이라고 입력하고 파일을 실행하면 매개변수가 함께 출력 됨
print(sys.argv)

from datetime import datetime

now = datetime.now()
print(now.year)
# 1 ~ 12; 파이썬에서 month는 0~11이 아니라 사람이 인지하는 월 그대로 출력된다. 
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

date1 = datetime(2000, 1, 1, 1, 1, 1)
print(date1.year)
print(date1.month)
print(date1.day)
print(date1.hour)
print(date1.minute)
print(date1.second)