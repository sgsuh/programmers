#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 22:29:39 2018

@author: sgsuh
"""

"""
strToInt 메소드는 String형 str을 매개변수로 받습니다.
str을 숫자로 변환한 결과를 반환하도록 strToInt를 완성하세요.
예를들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.
str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.
"""

def strToInt(str):
    result = 0
    #함수를 완성하세요
    
    if str[0] == "-":
        length = len(str) - 1
        
        for i in range(length):
            idx = len(str) - 1 - i
            mul = 10**i
            result += int(str[idx]) * mul
            
        result *= -1
            
    else:
        length = len(str)
        
        for i in range(length):
            idx = len(str) - 1 - i
            mul = 10**i
            result += int(str[idx]) * mul
            
    
    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"));
