def solution(n):
    answer = 0
    current = 6
    while current % n != 0:
        current += 6
    answer = current // 6
    return answer