#직사각형의 넓이를 구하는 클래스
class Rect:
  def __init__(self, width, height):
    if width <= 0 or height <= 0:
      raise Exception("너비와 높이는 음수가 나올 수 없습니다.")
    self.width = width
    self.height = height
  def get_area(self):
    return self.width * self.height

rect = Rect(10, 10)
#길이에는 음수가 존재하지 않는데 아래와 같이 외부에서 음수를 넣어 줌으로써 에러 발생 가능하다.
rect.width = -10
print(rect.get_area())


#외부에서 변경이 불가능 하도록 하는 방법
class Rect2:
  def __init__(self, width, height):
    if width <= 0 or height <= 0:
      raise Exception("너비와 높이는 음수가 나올 수 없습니다.")
    self.__width = width
    self.__height = height
  def get_area(self):
    return self.__width * self.__height

rect2 = Rect2(10, 10)
#길이 앞에 "__"를 붙여 줌으로써 외부 변경이 불가능하게 된다.
rect2.__width = -10
print(rect2.get_area())