def solution(numbers):
    n = list(map(int, numbers))
    n = sorted(n)
    for i in range(len(numbers)):
        mul = n[i] * n[i-1]
        mul2 = n[-i] * n[-i-1]
    if mul > mul2:
        answer = mul
    else:
        answer = mul2
    return answer