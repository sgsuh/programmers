#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 22:09:22 2018

@author: sgsuh
"""

"""
rm_small함수는 list타입 변수 mylist을 매개변수로 입력받습니다.
mylist 에서 가장 작은 수를 제거한 리스트를 리턴하고, mylist의 원소가 1개 이하인 경우는 []를 리턴하는 함수를 완성하세요.
예를들어 mylist가 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10, 8, 22]면 [10, 22]를 리턴 합니다.
"""

def rm_small(mylist):
    # 함수를 완성하세요
    answer = []
    
    min_val = min(mylist)
    idx = mylist.index(min_val)
    
    for i in range(len(mylist)):
        if i == idx:
            continue
        else:
            answer.append(mylist[i])
    
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
#my_list = [4, 3, 2, 1]
my_list = [10, 8, 22]
print("결과 {} ".format(rm_small(my_list)))