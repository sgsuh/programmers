"""
그렙시에는 0으로 된 도로에 숫자 블록을 설치하기로 하였습니다. 
숫자 블록의 규칙은 다음과 같습니다.

블록의 번호가 n 일 때, 가장 처음 블록은 n * 2번째 위치에 설치합니다. 
그다음은 n * 3, 그다음은 n * 4, ...로 진행합니다.
만약 기존에 블록이 깔려있는 자리라면 그 블록을빼고 새로운 블록으로 집어넣습니다.

예를 들어 1번 블록은 2,3,4,5, ... 인 위치에 우선 설치합니다. 
그다음 2번 블록은 4,6,8,10, ... 인 위치에 설치하고, 3번 블록은 6,9,12... 인 위치에 설치합니다.

이렇게 3번 블록까지 설치하고 나면 첫 10개의 블록은 0, 1, 1, 2, 1, 3, 1, 2, 3, 2이됩니다.

그렙시는 길이가 1,000,000,000인 도로에 1번 블록부터 시작하여 10,000,000번 블록까지 
위의 규칙으로 모두 놓았습니다.

그렙시의 시장님은 특정 구간의 어떤 블록이 깔려 있는지 알고 싶습니다.

구간을 나타내는 두 수 begin, end 가 매개변수로 주어 질 때, 
그 구간에 깔려 있는 블록의 숫자 배열(리스트)을 return하는 solution 함수를 완성해 주세요.
제한 사항

    begin, end 는 1 이상 1,000,000,000이하의 자연수 이고, begin는 항상 end보다 작습니다.
    end - begin 의 값은 항상 1,000을 넘지 않습니다.

입출력 예
begin 	end 	result
1 	    10 	    [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]
"""

"""
Case1
"""
# def solution(begin, end):
#     answer = []

#     for i in range(begin, end+1):
#         if i == 1:
#             answer.append(0)
#             continue

#         if i % 2 == 0:
#             answer.append(int(i/2))
#         else:
#             div = int(i/2)

#             for j in range(div, 0, -1):

#                 if i % j == 0:
#                     answer.append(j)
#                     break

#     return answer

"""
Case2
"""
def block(n):
    max_val = 0

    for i in range(2, n+1):
        if n % i == 0:

            if n / i <= 10000000:
                return int(n/i)

            max_val = i

        if i*i > n:
            break

    if max_val > 0:
        return max_val

    else:
        return 1

def solution(begin, end):
    answer = []

    for i in range(begin, end+1):
        if i == 1:
            answer.append(0)
            continue

        answer.append(block(i))

    return answer

print(solution(1, 10))