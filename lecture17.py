number = 0 # 나중에!

if number != 0:
    # some codes
    # pass를 적으면 특별한 코드 작성 없이도 구문과 관련된 오류 없이 실행이 되게 된다
    pass
else:
    # some codes
    pass

year = int(input("태어난 해를 입력해 주세요> "))

if year % 12 == 0:
    print("원숭이 띠 입니다.")
elif year % 12 == 1:
    print("닭 띠 입니다.")
elif year % 12 == 2:
    print("개 띠 입니다.")
elif year % 12 == 3:
    print("돼지 띠 입니다.")
elif year % 12 == 4:
    print("쥐 띠 입니다.")
elif year % 12 == 5:
    print("소 띠 입니다.")
elif year % 12 == 6:
    print("범 띠 입니다.")
elif year % 12 == 7:
    print("토끼 띠 입니다.")
elif year % 12 == 8:
    print("용 띠 입니다.")
elif year % 12 == 9:
    print("뱀 띠 입니다.")
elif year % 12 == 10:
    print("말 띠 입니다.")
else:
    print("양 띠 입니다.")