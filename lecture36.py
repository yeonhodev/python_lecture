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

#함수를 사용하는 이유
#함수를 사용하지 않은 경우
print("<p>{}</p>".format("안녕하세요."))
print("<p>{}</p>".format("간단한 HTML 태그를 만드는 예입니다."))

#Ouput
#<p>안녕하세요.</p>
#<p>간단한 HTML 태그를 만드는 예입니다.</p>

#그런데 갑자기 '단순한 <p></p>로 감싸지 말고, <p class='content-line'></p>로 감싸주세요'라는 요청을 받았다면, 함수를 사용하지 않은 상태에서는 모든 코드를 하나하나 수정해야 한다. -> 실수 발생 가능

#함수를 사용한 경우 -> 협업 및 유지보수에 유리하다.
#p 태그로 감싸는 함수

def p(content):
    #기존 코드 주석 처리
    #return "<p>{}</p>".format(content)
    # 2020.07.08 요청 반영
    return "<p class='content-line'>{}</p>".format(content)

#출력합니다. 
print(p("안녕하세요."))
print(p("간단한 HTML 태그를 만드는 예 입니다."))