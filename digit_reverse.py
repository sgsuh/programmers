#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 20:10:56 2018

@author: sgsuh
"""

"""
digit_reverse함수는 양의 정수 n을 매개변수로 입력받습니다.
n을 뒤집어 숫자 하나하나를 list로 표현해주세요
예를들어 n이 12345이면 [5,4,3,2,1]을 리턴하면 됩니다.
"""

def digit_reverse(n):
    # 함수를 완성해 주세요
    n = str(n)
    n = list(n)
    n.reverse()
    
    answer = []
    
    for i in range(len(n)):
        answer.append(int(n[i]))
    
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(digit_reverse(12345)));