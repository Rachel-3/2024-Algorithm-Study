import math

def solution(brown, yellow):
    total = brown + yellow
    
    for width in range(int(math.sqrt(total)), 0, -1):
        if total % width == 0:
            height = total // width
            if (width - 2) * (height - 2) == yellow:
                return [height, width]

print(solution(8, 1)) # [3, 3]
print(solution(24, 24)) # [8, 6]


''' 실패 '''
'''
정확성: 53.8
합계: 53.8 / 100.0

import math
def solution(brown, yellow):
    answer = []
    xy = brown + yellow
    xy_sqrt = math.sqrt(xy)
    y = int(xy_sqrt)
    for i in range(brown) :
        if i * y == xy :
            answer.append(i)
            break
    answer.append(y)
    return answer
'''