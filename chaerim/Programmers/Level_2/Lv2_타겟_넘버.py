def solution(numbers, target):
    answer = 0

    stack = [(0, 0)]

    while stack:
        index, number_sum = stack.pop()

        if index == len(numbers):
            if number_sum == target:
                answer += 1
        else:
            stack.append((index + 1, number_sum + numbers[index]))
            stack.append((index + 1, number_sum - numbers[index]))

    return answer