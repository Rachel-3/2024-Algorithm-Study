import math
def solution(n):
    answer = 0
    i = 1
    while True :
        if math.factorial(i) > n :
            break
        else :
            i += 1
    return i - 1