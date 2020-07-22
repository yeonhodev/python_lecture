"""
- 스네이크 케이스
i_love_you : 기본적으로 사용

- 케멀 케이스 : Student
ILoveYou : 클래스 이름에만 사용 (파이썬에서는 소문자로 시작하는 케멀 케이스를 사용하지 않는다.)
"""

class Student:
  # 생성자
  def __init__(self, name, age):
    print("객체가 생성되었습니다.")
    self.name = name
    self.age = age

  # 소멸자 : 소멸자는 잘 사용하지 않지만, 이런게 있다고만 알면 됨.
  def __del__(self):
    print("객체가 소멸되었습니다.")
  
  # 함수 선언하기
  def 출력(self):
    print(student.name, student.name, student.age, student.age)

student = Student("윤인성", 3)
print(student.name, student.age)
student.출력()
# 클래스(틀): 학생은 이름이라는 속성을 가지고 있어!
# 객체(실체화 된 것): 학생 이름은 "윤인성"이야!
# 실체화 한 객체 = "인스턴스"