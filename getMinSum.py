#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 23:44:53 2018

@author: sgsuh
"""

"""
자연수로 이루어진 길이가 같은 수열 A,B가 있습니다. 
최솟값 만들기는 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱한 값을 누적하여 더합니다. 
이러한 과정을 수열의 길이만큼 반복하여 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다.

예를 들어 A = [1, 2] , B = [3, 4] 라면

    A에서 1, B에서 4를 뽑아 곱하여 더합니다.
    A에서 2, B에서 3을 뽑아 곱하여 더합니다.

수열의 길이만큼 반복하여 최솟값 10을 얻을 수 있으며, 이 10이 최솟값이 됩니다.
수열 A,B가 주어질 때, 최솟값을 반환해주는 getMinSum 함수를 완성하세요.
"""

def getMinSum(A,B):
    answer = 0

    A.sort()
    B.sort()
    
    for i in range(len(A)):
        answer += A[i] * B[len(A)-1-i]

    return answer

#아래 코드는 출력을 위한 테스트 코드입니다.

print(getMinSum([1,2],[3,4]))