#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 19:21:09 2018

@author: sgsuh
"""

"""
numberOfPrime 메소드는 정수 n을 매개변수로 입력받습니다.

1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하도록 numberOfPrime 메소드를 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

10을 입력받았다면, 1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환
5를 입력받았다면, 1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환
"""

def numberOfPrime(n):
    # 1부터 n사이의 소수는 몇 개인가요?
    answer = 0
    
    for i in range(2,n+1):
        if i==2 or i==3 or i==5 or i==7 or i==11 or i==13 or i==17 or i==19:
            answer += 1
            continue
        
        if i%2 == 0:
            continue
        elif i%3 == 0:
            continue
        elif i%5 == 0:
            continue
        elif i%7 == 0:
            continue
        elif i%11 == 0:
            continue
        elif i%13 == 0:
            continue
        elif i%17 == 0:
            continue
        elif i%19 == 0:
            continue
        
        flag = 1
        for j in range(2,i):
            if i%j == 0:
                flag = 0
                break
            
        if flag == 1:
            answer += 1

            
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numberOfPrime(10))