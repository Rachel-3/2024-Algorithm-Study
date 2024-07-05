def solution(arr):
    answer = []

    for number in arr:
        for _ in range(number):
            answer.append(number)

    return answer