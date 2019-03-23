#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 23:53:32 2018

@author: sgsuh
"""

"""
Jaden_Case함수는 문자열 s을 매개변수로 입력받습니다.
s에 모든 단어의 첫 알파벳이 대문자이고, 그 외의 알파벳은 소문자인 문자열을 리턴하도록 함수를 완성하세요
예를들어 s가 "3people unFollowed me for the last week"라면 "3people Unfollowed Me For The Last Week"를 리턴하면 됩니다.
"""

def Jaden_Case(s):
    # 함수를 완성하세요
    answer = ''
    
    for i in range(len(s)):
        if i == 0:
            if s[i].islower():
                answer += s[i].upper()
            else:
                answer += s[i]
        else:
            if s[i-1] == ' ':
                if s[i].islower():
                    answer += s[i].upper()
                else:
                    answer += s[i]
            else:
                if s[i].isupper():
                    answer += s[i].lower()
                else:
                    answer += s[i]
    return answer
    
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))