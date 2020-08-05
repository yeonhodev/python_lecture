from flask import Flask
app = Flask(__name__)

@app.route("/") # 데코레이터(@으로 시작함) : 어떤 함수에 "미리 만든 규격화된 처리"를 적용할 때 사용하는 것
# 함수 데코레이터: 함수로 만든 데코레이터
# 클래스 데코레이터: 클래스로 만든 데코레이터
def hello():
  return "<h1>Hello World!</h1>"