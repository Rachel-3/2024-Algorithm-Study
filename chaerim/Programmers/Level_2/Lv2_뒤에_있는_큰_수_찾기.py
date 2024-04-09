def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            last = stack.pop()
            answer[last] = number
        stack.append(i)

    return answer

'''시간 초과
def solution(numbers):
    answer = []

    number_max = max(numbers)

    for number in range(len(numbers)):
        larger_number = -1

        if numbers[number] < number_max:
            for i in range(number+1, len(numbers)):
                if numbers[i] > numbers[number]:
                    larger_number = numbers[i]
                    break

        answer.append(larger_number)

    return answer
'''