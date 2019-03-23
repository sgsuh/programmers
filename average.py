#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 23:25:01 2018

@author: sgsuh
"""

"""
함수를 완성해서 매개변수 array의 평균값을 return하도록 만들어 보세요.
어떠한 크기의 array가 와도 평균값을 구할 수 있어야 합니다.
"""

def average(array):
    # 함수를 완성해서 매개변수 array의 평균값을 return하도록 만들어 보세요.
    
    length = len(array)
    answer = 0
    
    for i in range(length):
        answer += array[i]
        
    answer /= length

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
list = [5,3,4] 
print("평균값 : {}".format(average(list)));
