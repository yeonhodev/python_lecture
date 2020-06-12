import datetime

now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

if now.hour < 12:
    print("it's {}:{}. It's morning.".format(now.hour, now.minute))
if now.hour >= 12:
    print("it's {}:{}. It's afternoon.".format(now.hour, now.minute))

if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄 입니다.".format(now.month))
if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름 입니다.".format(now.month))
if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을 입니다.".format(now.month))
if now.month == 12 or now.month <= 2:
    print("이번 달은 {}월로 겨울 입니다.".format(now.month))


number = input("Choose a integer: ")

#Even and Odd
number = number[-1]
number = int(number)

if number % 2 == 0:
    print("It's an even number.")

if number % 2 == 1:
    print("It's an odd number.")