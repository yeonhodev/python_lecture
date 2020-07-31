# 확인문제 : 현재 디렉터리를 읽어 들이고 파일인지 디렉터리인지 구분하기
# 모듈을 읽어 들입니다. 
import os

# 현재 폴더의 파일/폴더를 출력합니다.
output = os.listdir(".")
print("os.listdir():", output)
print()

# 현재 폴더의 파일/폴더를 구분합니다. 
print("# 폴더와 파일 구분하기")
for path in output:
  if os.path.isdir(path):
    print("폴더:", path)
  else:
    print("파일:", path)


# 확인 문제: 재귀함수로 만들어서 리스트를 평탄화하는 함수를 만들어 보세요. 리스트 평탄화(flatten)는 중첩된 리스트가 있을 때 중첩을 모두 제거하고 풀어서 1차원 리스트로 만드는 것을 의미합니다. 

def flatten(data):
  output = []
  for item in data:
    if type(item) == list:
      output += flatten(item)
    else:
      output.append(item)
  return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본: ", example)
print("변환: ", flatten(example))

#  확인 문제: 이를 활용해 "폴더라면 또 탐색하기"라는 재귀 구성으로 현재 폴더 내부에 있는 모든 파일을 탐색하도록 코드를 작성해 보세요. 
# 모듈을 읽어 들입니다. 
import os

# 폴더의 요소 읽어 들이는 함수
def read_folder(path):
  print(path)
  # 폴더의 요소 읽어 들이기
  output = os.listdir(path)
  # 폴도의 요소 구분하기
  for item in output:
    if os.path.isdir(path + "/" + item):
      # 폴더라면 계속 읽어 들이기
      read_folder(path + "/" + item)
    else:
      # 파일이라면 출력하기
      pass
      #print("파일: ", item)

# 현재 폴더의 파일/폴더를 출력합니다. 
read_folder(".")