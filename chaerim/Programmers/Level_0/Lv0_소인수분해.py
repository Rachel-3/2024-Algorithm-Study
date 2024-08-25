def solution(n):
    answer = []

    i = 2
    while i * i <= n:
        if n % i == 0:
            if i not in answer:
                answer.append(i)
            n //= i
        else:
            i += 1
    
    if n > 1 and n not in answer:
        answer.append(n)

    return answer