def solution(a, b, n):
    answer = 0

    while n >= a:
        div = n // a
        remainder = n % a

        n = (div * b) + remainder
        answer += div * b

    return answer