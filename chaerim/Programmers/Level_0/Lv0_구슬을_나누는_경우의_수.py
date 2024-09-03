def factorial(n):
    start = 1
    for i in range(1, n + 1):
        start *= i
    return start

def solution(balls, share):
    answer = factorial(balls) // (factorial(share) * factorial(balls - share))
    return answer