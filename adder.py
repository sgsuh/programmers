#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 20:27:24 2018

@author: sgsuh
"""

"""
adder함수는 정수 a, b를 매개변수로 입력받습니다.
두 수와 두 수 사이에 있는 모든 정수를 더해서 리턴하도록 함수를 완성하세요. 
a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
예를들어 a가 3, b가 5이면 12를 리턴하면 됩니다.

a, b는 음수나 0, 양수일 수 있으며 둘의 대소 관계도 정해져 있지 않습니다.
"""

def adder(a, b):
    # 함수를 완성하세요
    if a>b:
        l = a
        s = b
    else:
        l = b
        s = a
        
    answer = 0
    
    for i in range(s, l+1):
        answer += i
        
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))