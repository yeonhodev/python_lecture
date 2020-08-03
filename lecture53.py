# BeautifulSoup 모듈 = 라이브러리
# Flask 모듈 = 프레임워크

# 구글에서 "python flask github" 검색
# pip install Flask 설치 후 -> 파이썬 실행 후 "import flask"를 통해 모듈이 제대로 설치 되었는지 확인한다. 

from flask import Flask
app = Flask(__name__)

@app.route("/") # 데코레이터 : 다다음 강의에서 설명 다시 할 예정
def hello():
    return "<h1>안녕하세요!</h1>"


"""
윈도우의 경우; 아래의 명령어를 터미널에서 실행
set FLASK_APP=lecture53.py # (환경) 변수를 설정하는 부분(터미널을 실행하고 한번만!)
flask run                  # flask 명령

맥의 경우; 아래의 명령어를 터미널에서 실행
export FLASK_APP=lecture53.py # (환경) 변수를 설정하는 부분(터미널을 실행하고 한번만!)
flask run                  # flask 명령
"""

# 라이브러리: 정상적인 제어방법으로 사용하는 모듈
# 프레임워크: 제어 역전(IoC)이 일어나는 모듈 
# 정상적인 제어 = 개발자가 모듈을 import 해서 직접 사용한다. 
# 제어 역전(Inversion of Control:IoC) = 모듈이 개발자의 코드를 사용한다. 

# 라이브러리는 보통 처음 보더라도 잘 사용하는데, 프레임워크는 처음 보고 "왜 Python 명령어를 사용하지 않고 이상한 걸 사용해?"라는 방응이 있을 수 있다. 