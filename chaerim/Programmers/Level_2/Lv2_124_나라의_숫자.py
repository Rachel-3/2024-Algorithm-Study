def solution(n):
    answer = ''

    while n > 0:
        n -= 1
        share = n // 3
        rest = n % 3
        answer = '124'[rest] + answer
        n = share

    return answer