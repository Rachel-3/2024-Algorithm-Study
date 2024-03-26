import math

def solution(a, b):
    answer = [2, 5]
    b = b / (math.gcd(a, b))
    for i in answer :
        while not b % i :
            b = b // i
    if b == 1 :
        return 1
    else :
        return 2