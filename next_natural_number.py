#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 21:46:24 2018

@author: seukgyo
"""

"""
자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

    조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
    조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
    조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.

예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.
제한 사항

    n은 1,000,000 이하의 자연수 입니다.

입출력 예
n 	result
78 	83
15 	23
입출력 예 설명

입출력 예#1
문제 예시와 같습니다.
입출력 예#2
15(1111)의 다음 큰 숫자는 23(10111)입니다.
"""

def solution(n):
    answer = 0
    
    src_bin_num = 0
    
    src = n
    
    while src>0:
        if src%2==1:
            src -= 1
            src_bin_num += 1
            
        src /= 2
    
    for i in range(int(n+1), 1000001):
        dst_bin_num = 0
        
        dst = i
        
        while dst>0:
            if dst%2==1:
                dst -= 1
                dst_bin_num += 1
                
            dst /= 2
        
        if dst_bin_num == src_bin_num:
            break
    
    answer = i
    
    return answer

print(solution(78))
print(solution(15))