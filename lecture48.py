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


#변경이 완전히 불가하면 불편해서 나온 방법이 Getter와 Setter이다. -> "get_" 과 "set_"으로 시작하는 함수 -> Getter와 Setter는 선별적으로 필요에 따라 만들어 사용하면 된다. 
class Rect3:
  def __init__(self, width, height):
    if width <= 0 or height <= 0:
      raise Exception("너비와 높이는 음수가 나올 수 없습니다.")
    self.__width = width
    self.__height = height

  #아래의 코드를 통해 너비와 높이를 굉장히 안전하게 사용할 수 있다. 
  def get_width(self):
    return self.__width
  def set_width(self, width):
    if width <= 0:
      raise Exception("너비는 음수가 나올 수 없습니다.")
    self.__width = width

  def get_height(self):
    return self.__height
  def set_height(self, height):
    if height <= 0:
      raise Exception("높이는 음수가 나올 수 없습니다.")
    self.__height = height
  def get_area(self):
    return self.__width * self.__height

rect3 = Rect3(10, 10)
rect3.set_width(rect3.get_width() + 10)
print(rect3.get_area())

# 기본적인 속성: Attribute
# 어떤 처리를 해준 속성: Property

# Property를 활용해서 문제 해결하기
class Rect4:
  def __init__(self, width, height):
    if width <= 0 or height <= 0:
      raise Exception("너비와 높이는 음수가 나올 수 없습니다.")
    self.__width = width
    self.__height = height

  @property
  def width(self):
    return self.__width
  @width.setter
  def width(self, width):
    if width <= 0:
      raise Exception("너비는 음수가 나올 수 없습니다.")
    self.__width = width

  def get_height(self):
    return self.__height
  def set_height(self, height):
    if height <= 0:
      raise Exception("높이는 음수가 나올 수 없습니다.")
    self.__height = height
  def get_area(self):
    return self.__width * self.__height

rect4 = Rect4(10, 10)
#rect4.set_width(rect4.get_width() + 10)
rect4.width += 10
print(rect4.get_area())
