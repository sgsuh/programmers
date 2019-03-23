#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 22:53:00 2018

@author: sgsuh
"""

"""
printTriangle 메소드는 양의 정수 num을 매개변수로 입력받습니다.
다음을 참고해 *(별)로 높이가 num인 삼각형을 문자열로 리턴하는 printTriangle 메소드를 완성하세요
printTriangle이 return하는 String은 개행문자('\n')로 끝나야 합니다.
"""

def printTriangle(num):
    s = ""
    #함수를 완성하세요
    
    for i in range(num):
        for j in range(i+1):
            s += "*"
            
        s += "\n"

    return s


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( printTriangle(3) )