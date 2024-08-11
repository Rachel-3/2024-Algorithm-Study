def solution(numbers, k):
    answer = 0

    for _ in range(k - 1):
        answer = (answer + 2) % len(numbers)

    return numbers[answer]