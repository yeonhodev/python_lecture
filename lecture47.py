class Student:
  def __str__(self):
    return "{} {}살".format(self.name, self.age)
  def __init__(self, name, age):
    print("객체가 생성되었습니다.")
    self.name = name
    self.age = age
  def __del__(self):
    print("객체가 소멸되었습니다.")
  def 출력(self):
    print(student.name, student.age)

student = Student("윤인성", 3)
student.출력()
print(str(student))


class Student2:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __eq__(self, other):
    print("eq() 함수")
  def __ne__(self, other):
    print("ne() 함수")
  def __gt__(self, other):
    print("gt() 함수")
  def __ge__(self, other):
    print("ge() 함수")
  def __lt__(self, other):
    print("lt() 함수")
  def __le__(self, other):
    print("le() 함수")
  
student2 = Student2("윤인성", 3)
student2 == student2
student2 != student2
student2 > student2
student2 >= student2
student2 < student2
student2 <= student2
