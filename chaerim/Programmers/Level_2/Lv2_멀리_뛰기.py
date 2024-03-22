def solution(n):
    answer = 0

    if n == 1:
        answer = 1
    elif n == 2:
        answer = 2
    else:
        number_of_cases = [0]*(n+1)

        number_of_cases[1] = 1
        number_of_cases[2] = 2

        for i in range(3, n + 1):
            number_of_cases[i] = (number_of_cases[i - 1] + number_of_cases[i - 2]) % 1234567

        answer = number_of_cases[-1]

    return answer