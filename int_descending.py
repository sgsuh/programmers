#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 11:51:09 2018

@author: seukgyo
"""

"""
문제 설명

함수 solution은 정수 n을 매개변수로 입력받습니다. 
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
예를들어 n이 118372면 873211을 리턴하면 됩니다.
제한 조건

    n은 1이상 8000000000 이하인 자연수입니다.

입출력 예
n 	    return
118372 	873211
"""

def solution(n):
    answer = ''
    
    n = str(n)
    n = list(n)
    n.sort()
    n.reverse()
    
    for i in range(len(n)):
        answer += n[i]
        
    answer = int(answer)
    
    return answer

print(solution(118372))