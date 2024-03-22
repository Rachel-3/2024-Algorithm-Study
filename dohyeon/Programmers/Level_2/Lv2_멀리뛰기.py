''' 실패
채점 결과
정확성: 12.5
합계: 12.5 / 100.0
'''
from itertools import *
def solution(n):
    answer = 0
    dataset = [n + 1 for n in range(n)]
    for i in range(1, n + 1) :
        printList = list(product(dataset, repeat = i))
        for j in printList :
            if sum(j) == n :
                check = 0
                for k in j :
                    if k > 2 :
                        check = 1
                if check != 1 :
                    answer += 1
    return answer
