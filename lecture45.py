# 학생 리스트를 선언합니다.
students = [
  { "name": "윤인성", "korean": 87, "math": 98, "english": 88, "science": 95},
  { "name": "연하진", "korean": 92, "math": 98, "english": 96, "science": 98},
  { "name": "구지연", "korean": 76, "math": 96, "english": 94, "science": 90},
  { "name": "나선주", "korean": 98, "math": 92, "english": 96, "science": 92},
  { "name": "윤아린", "korean": 95, "math": 98, "english": 98, "science": 98},
  { "name": "윤명월", "korean": 64, "math": 88, "english": 92, "science": 92}
]

# 학생을 한명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
  # 점수의 총합과 평균을 구합니다.
  score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
  score_average = score_sum / 4
  # 출력합니다.
  print(student["name"], score_sum, score_average, sep="\t")

print()



# 위의 코드를 함수로 똑같이 구현하기 -> 행위 정하기
def 학생_생성(name, korean, math, english, science):
  return{
    "name": name,
    "korean": korean,
    "math": math,
    "english": english,
    "science": science
  }

def 총점(student):
  return student["korean"] + student["math"] + student["english"] + student["science"]
def 평균(student):
  return 총점(student) / 4
def 출력(student):
  print(student["name"], 총점(student), 평균(student), sep="\t")

#---------------------------------------- #
#학생 리스트를 선언합니다.
students = [
  학생_생성("윤인성", 87, 98, 88, 95),
  학생_생성("연하진", 92, 98, 96, 98),
  학생_생성("구지연", 76, 96, 94, 90),
  학생_생성("나선주", 98, 92, 96, 92),
  학생_생성("윤아린", 95, 98, 98, 98),
  학생_생성("윤명월", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
  출력(student)