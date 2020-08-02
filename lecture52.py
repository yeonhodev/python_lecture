# 외부 모듈 설치
# pip install 모듈이름
# pip install 모듈이름==1.0.0
# alias python=python3
# alias pip=pip3

html_doc = """
<html>
  <head>
    <title>TEST PAGE</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
"""

from urllib import request
from bs4 import BeautifulSoup

# "기상청 rss"로 검색 후 제일 위에 있는 링크에서 서울.경기도 RSS를 클릭해서 생긴 URL 복사 붙여 넣기. 
content = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.select("h1"))
print(soup.select("h1")[0].string)

soup1 = BeautifulSoup(content, 'html.parser')
print(soup1.select("data"))

for data in soup1.select("data"):
  print(data)
  print("시간:", data.select_one("tmef").string)
  print("날씨:", data.select_one("wf").string)
  print("-" * 20)