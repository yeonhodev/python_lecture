# 모듈 불러오는 방법1 -> 가장 원초적인 방법
#math = __import__("math")
#print(math.pi)
#print(math.sin(10))

# 모듈 불러오는 방법2 (추천하는 방법) -> 에디터를 사용하며 모듈 뒤에 "."을 찍으면 미리보기 등 여러가지 편리한 기능 제공함
import math
print(math.pi)
print(math.sin(10))

# 모듈 불러오기 3; import as
# 수학 = __import__("math")
import math as 수학 # 바로 윗줄과 정확하게 같은 의미의 코드 
print(수학.pi)
print(수학.sin(10))

# 모듈 불러오기 4; from import ; "math." 입력 없이 바로 기능 사용 가능
from math import pi, sin
print(pi)
print(sin(10))

# 모듈 불러오기 5; from import * -> math가 가지고 있는 모든 기능들을 들고 오겠다
# 이름 충돌이 일어나 기능을 사용할 수 없게 될 수 있으므로 주의가 필요하다. 
from math import *
print(pi)
print(sin(10))