#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 23:20:07 2018

@author: sgsuh
"""

"""
numPY함수는 대문자와 소문자가 섞여있는 문자열 s를 매개변수로 입력받습니다.
s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 리턴하도록 함수를 완성하세요. 
'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다.
예를들어 s가 "pPoooyY"면 True를 리턴하고 "Pyy"라면 False를 리턴합니다.
"""

def numPY(s):
    # 함수를 완성하세요
    
    length = len(s)
    numP = 0
    numY = 0
    
    for i in range(length):
        if s[i] == 'p' or s[i] == 'P':
            numP += 1
        elif s[i] == 'y' or s[i] == 'Y':
            numY += 1
            
    if numP > 0 or numY > 0:
        if numP == numY:
            return True
        else:
            return False
    
    return True



# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )