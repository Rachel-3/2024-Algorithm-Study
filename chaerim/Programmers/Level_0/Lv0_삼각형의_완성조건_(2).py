def solution(sides):
    answer = 0

    a, b = sides

    answer += min(a, b) 

    answer += (a + b) - max(a, b) - 1

    return answer