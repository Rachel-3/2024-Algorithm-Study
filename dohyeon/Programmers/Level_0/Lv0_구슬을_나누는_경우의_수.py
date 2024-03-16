import math
    
def solution(balls, share):
    answer = math.factorial(balls) / ((math.factorial(balls - share)) * math.factorial(share))
    return answer