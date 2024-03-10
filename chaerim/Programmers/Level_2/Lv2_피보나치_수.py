def solution(n):
    answer = 0

    fibonacci = []
    for i in range(0, n+1):
        if i == 0:
            fibonacci.append(0)
        elif i == 1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[i-2] + fibonacci[i-1])

    answer = fibonacci[n]%1234567

    return answer