def solution(n):
    answer = 1
    for i in range(1, n // 2 + 1):
        total = 0
        while total < n:
            total += i
            if total == n:
                answer += 1
                break
            i += 1
    return answer