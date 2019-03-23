#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 20:48:46 2018

@author: sgsuh
"""

"""
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 
예를 들어 2와 7의 최소공배수는 14가 됩니다. 
정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. 
nlcm 함수를 통해 n개의 숫자가 입력되었을 때, 최소공배수를 반환해 주세요. 예를들어 [2,6,8,14] 가 입력된다면 168을 반환해 주면 됩니다.
"""

def nlcm(num):
    answer = 1
    
    cm = []
    
    i = 2
    
    while(i < max(num)):
        count = 0
        flag = 0
        
        for j in range(len(num)):
            if num[j]>=i and num[j]%i == 0:
                count += 1
                
            if count >= 2:
                flag = 1
                cm.append(i)
                break
                
        if flag == 1:
            for j in range(len(num)):
                if num[j]>=i and num[j]%i == 0:
                    num[j] = int(num[j] / i)
                    
            i = 1
                    
        i += 1
                    
    for i in range(len(num)):
        if num[i] != 1:
            cm.append(num[i])

    for i in range(len(cm)):
        answer *= cm[i]
        
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2,6,8,14]));