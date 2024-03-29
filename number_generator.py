#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 23:13:18 2018

@author: sgsuh
"""

"""
number_generator함수는 x와 n을 입력 받습니다.
2와 5를 입력 받으면 2부터 시작해서 2씩 증가하는 숫자를 5개 가지는 리스트를 만들어서 리턴합니다.
[2,4,6,8,10]

4와 3을 입력 받으면 4부터 시작해서 4씩 증가하는 숫자를 3개 가지는 리스트를 만들어서 리턴합니다.
[4,8,12]

이를 일반화 하면 x부터 시작해서 x씩 증가하는 숫자를 n개 가지는 리스트를 리턴하도록 함수 number_generator를 완성하면 됩니다.
"""

def number_generator(x, n):
    # 함수를 완성하세요
    
    answer = []
    
    for i in range(n):
        answer.append(x*(i+1))
        
    
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(number_generator(3,5))