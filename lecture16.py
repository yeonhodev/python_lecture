import datetime
now = datetime.datetime.now()

if 3 <= now.month <=5:
    print("It's Spring.")
elif 6 <= now.month <=8:
    print("It's Summer.")
elif 9 <= now.month <=11:
    print("It's Fall.")
else:
    print("It's Winter.")

score = float(input("> Type your score: "))

if score == 4.5:
    print("God")
elif 4.2 <= score:
    print("Love of professer.")
elif 3.5 <= score:
    print("Extraordinary")
elif 2.5 <= score:
    print("Normal")
else:
    print("Try harder!") 