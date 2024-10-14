def solution(array, commands):
    answer = []

    for command in commands:
        start, end, number = command
        new_command = sorted(array[start-1:end])
        answer.append(new_command[number-1])

    return answer