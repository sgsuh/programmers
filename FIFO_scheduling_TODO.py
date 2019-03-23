"""
처리해야 할 동일한 작업이 n 개가 있고, 이를 처리하기 위한 CPU가 있습니다.

이 CPU는 다음과 같은 특징이 있습니다.

    CPU에는 여러 개의 코어가 있고, 코어별로 한 작업을 처리하는 시간이 다릅니다.
    한 코어에서 작업이 끝나면 작업이 없는 코어가 바로 다음 작업을 수행합니다.
    2개 이상의 코어가 남을 경우 앞의 코어부터 작업을 처리 합니다.

처리해야 될 작업의 개수 n과, 각 코어의 처리시간이 담긴 배열 cores 가 매개변수로 주어질 때, 
마지막 작업을 처리하는 코어의 번호를 return 하는 solution 함수를 완성해주세요.
제한 사항

    코어의 수는 10,000 이하 2이상 입니다.
    코어당 작업을 처리하는 시간은 10,000이하 입니다.
    처리해야 하는 일의 개수는 50,000개를 넘기지 않습니다.

입출력 예
n 	cores 	result
6 	[1,2,3] 	2
"""

"""
Case1 : BigO(n * cores.size)
def solution(n, cores):
    answer = 0

    if len(cores) >= n:
        return n

    temp = []

    # Init
    for i in range(len(cores)):
        temp.append(cores[i])

    n -= len(cores)

    while n > 0:

        if temp.count(0) == 0:
            for i in range(len(temp)):
                temp[i] -= 1

        else:
            idx = temp.index(0)
            
            n -= 1
            answer = idx + 1

            temp[idx] = cores[idx]

            if n == 0:
                return answer

    return answer
"""

"""
Case3: Parametric Search, BigO(log n)
"""
def solution(n, cores):
    answer = 0

    # min_core = 10000

    if n <= len(cores):
        return n

    # for i in range(len(cores)):
    #     if min_core > cores[i]:
    #         min_core = cores[i]

    min_core = min(cores[:])

    min_time = int(n / len(cores) * min_core)
    max_time = n * min_core
    mid_time = int((min_time + max_time) / 2)

    while min_time < max_time:
        count = 0
        available_count = 0

        for i in range(len(cores)):
            count += int(mid_time / cores[i]) + 1

            if (mid_time % cores[i]) == 0:
                available_count += 1
                count -= 1

        if count >= n:
            max_time = mid_time

        elif (count + available_count) < n:
            min_time = mid_time + 1

        else:
            for i in range(len(cores)):

                if (mid_time % cores[i]) == 0:
                    count += 1

                if count == n:
                    return i + 1
        
        mid_time = int((min_time + max_time) / 2)

    return answer

print(solution(6, [1,2,3]))
