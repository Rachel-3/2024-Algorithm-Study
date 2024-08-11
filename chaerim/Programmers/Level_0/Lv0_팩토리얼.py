def solution(n):
    answer = 0

    start = 1
    while start <= n:
        answer += 1
        start *= answer

    return answer-1