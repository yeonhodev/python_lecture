#재귀함수로 리스트를 평탄화 하는 함수를 만듬. 리스트 평탄화(flatten)는 중첩된 리스트가 있을 때 중첩을 모두 제거하고 풀어서 1차원 리스트로 만드는 것을 의미합니다. 

def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            #output.append(item)
            output += [item]
    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))

#주석을 잘 다는 것이 코드를 잘 작성하는 것이다. 하지만, 함수를 잘 사용하면, 주석 조차도 필요 없을 만큼 가독성이 좋아진다. -> 훌륭한 예는 아래와 같다.

#함수 정의
# 상수는 아래의 PI와 같이 변수로 따로 빼서 설정해 주는 것이 좋다. 
PI = 3.14
def number_input():
    output = input("숫자 입력> ")
    return float(output)
def get_circumference(radius):
    return 2 * PI * radius
def get_circle_area(radius):
    return PI * radius * radius

#코드 본문
radius = number_input()
print(get_circumference(radius))
print(get_circle_area(radius))