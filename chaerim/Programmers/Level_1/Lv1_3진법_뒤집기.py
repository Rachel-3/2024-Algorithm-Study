def solution(n):
    answer = ''

    while n > 0:
        answer = str(n % 3) + answer
        n //= 3
    
    answer = answer[::-1]

    answer = int(answer, 3)

    return answer