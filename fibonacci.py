#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:39:51 2018

@author: sgsuh
"""

"""
피보나치 수는 F(0) = 0, F(1) = 1일 때, 2 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 점화식입니다. 
2 이상의 n이 입력되었을 때, fibonacci 함수를 제작하여 n번째 피보나치 수를 반환해 주세요. 
예를 들어 n = 3이라면 2를 반환해주면 됩니다.
"""

flag = 0
init_num = 0


def fibonacci(num):
    answer = 0

    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 1
    elif num == 3:
        return 2
    elif num == 4:
        return 3
    elif num == 5:
        return 5
    elif num == 6:
        return 8
    elif num == 7:
        return 13
    else:
#        answer = fibonacci(num-1) + fibonacci(num-2)
        answer = 2*fibonacci(num-2) + fibonacci(num-3)
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))