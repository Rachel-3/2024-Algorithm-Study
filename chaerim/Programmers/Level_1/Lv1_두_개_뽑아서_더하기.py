def solution(numbers):
    answer = []

    numbers_len = len(numbers)
    for i in range(numbers_len):
        for j in range(i + 1, numbers_len):
            n_sum = numbers[i] + numbers[j]
            if n_sum not in answer:
                answer.append(n_sum)

    answer = sorted(answer)

    return answer