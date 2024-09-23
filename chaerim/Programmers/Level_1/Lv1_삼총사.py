def solution(number):
    answer = 0

    number_len = len(number)
    for i in range(number_len - 2):
        for j in range(i + 1, number_len - 1):
            for k in range(j + 1, number_len):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1

    return answer