#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 23:13:21 2018

@author: sgsuh
"""

"""
앞뒤를 뒤집어도 똑같은 문자열을 palindrome이라고 합니다.
longest_palindrom함수는 문자열 s를 매개변수로 입력받습니다.
s의 부분문자열중 가장 긴 palindrom의 길이를 리턴하는 함수를 완성하세요.
예를들어 s가 "토마토맛토마토"이면 7을 리턴하고 "토마토맛있어"이면 3을 리턴합니다.
"""

def longest_palindrom(s):
    # 함수를 완성하세요
    l = len(s)
    
    if l == 1:
        return 1
    elif l == 2:
        return 2
    
    max_len = 2
    
    for i in range(l):
        for j in range(i+max_len, l):
            f = list(s[i:j+1])
            b = f.copy()
            b.reverse()
            
            if f == b:
                if len(f) > max_len:
                    max_len = len(f)
            
            
    if max_len == 2:
        max_len = 1
    
    
    return max_len


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(longest_palindrom("토마토맛토마토"))
print(longest_palindrom("토마토맛있어"))