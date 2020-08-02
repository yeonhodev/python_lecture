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

print(soup.select("h1"))
print(soup.select("h1")[0].string)