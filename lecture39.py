"""
텍스트 파일 처리 기본
 어떤 대상
 - 텍스트 파일: 텍스트 에디터로 열 수 있음
 - 바이너리 파일: 텍스트 에디터로 열 수 없음 (이미지, 동영상, 워드, 엑셀, PDF, etc)

 어떻게 다룰 것인가
 - 쓰기 
  - 새로(write): w
  - 있는 파일 뒤에(append): a
 - 읽기(read): r
"""

file = open("test.txt", "a")
#새로 작성한다는 뜻의 "w"를 적어 주면, 이제부터 write이라는 메소드로 글을 작성하는 것이 가능해 진다.
# "w" 대신 "a"를 사용하면 append가 돼서 파이썬 파일을 여러번 실행 해 주면 "안녕하세요."가 여러번 붙어 작성 된다.
file.write("안녕하세요.")

#파일을 모두 사용한 이후에는 클로즈를 반드시 해줘야 다른 프로그램에서 사용하려고 할 때 오류가 나지 않는다. 
file.close()

#파일 읽는 법
file = open("test.txt", "r")
print(file.read())
file.close()

#위의 코드들을 with 구문으로 줄여 쓰는 방법; close()를 따로 해주지 않아도 되어 편리함
with open("test.txt", "a") as file:
  file.write("안녕하세요.")

with open("test.txt", "r") as file:
  print(file.read())