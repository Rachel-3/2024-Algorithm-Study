def solution(l, r):
    answer = []

    for num in range(l, r + 1):
        if all(digit in ['5', '0'] for digit in str(num)):
            answer.append(num)

    return answer if answer else [-1]