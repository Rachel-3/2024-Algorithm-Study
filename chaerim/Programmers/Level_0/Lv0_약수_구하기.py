def solution(n):
    answer = []

    for num in range(1, n+1):
        if n%num == 0:
            answer.append(num)

    return answer