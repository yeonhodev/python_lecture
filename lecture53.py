# BeautifulSoup 모듈 = 라이브러리
# Flask 모듈 = 프레임워크

# 구글에서 "python flask github" 검색
# pip install Flask 설치 후 -> 파이썬 실행 후 "import flask"를 통해 모듈이 제대로 설치 되었는지 확인한다. 

from flask import Flask
app = Flask(__name__)

@app.route("/") # 데코레이터 : 다다음 강의에서 설명 다시 할 예정
def hello():
    return "Hello, World!"