def solution(n, m):
    answer = []

    a, b = n, m
    while b != 0:
        a, b = b, a%b

    answer.append(a)

    answer.append(abs(n*m) // a)

    return answer