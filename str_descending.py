#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 11:11:52 2018

@author: seukgyo
"""

"""
문제 설명

문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.
제한 사항

    str은 길이 1 이상인 문자열입니다.

입출력 예
s 	         return
"Zbcdefg" 	"gfedcbZ"
"""

def solution(s):
    answer = ''
    
    s = list(s)
    s.sort()
    s.reverse()
    
    for i in range(len(s)):
        answer += s[i]
    
    return answer

print(solution("Zbcdefg"))
