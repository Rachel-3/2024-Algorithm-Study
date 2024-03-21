import math
def solution(n,a,b):
    answer = 0
    a, b = min(a, b), max(a, b)
    round = math.log(n) / math.log(2)
    left = 1
    right = n
    
    while True :
        mid = math.floor((left + right) / 2)
        if((a >= left and a <= mid) and (b <= right and b > mid)) :
            return round
        if((a >= left and a <= mid) and (b >= left and b <= mid)) :
            right = mid
        else :
            left = mid
        round = round - 1
    return answer