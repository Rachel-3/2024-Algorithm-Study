def solution(n, t):
    answer = 0

    for i in range(1, t+1):
        n *= 2

    answer = n

    return answer