def solution(numbers, direction):
    answer = []
    if direction == "right" :
        answer.append(numbers[-1])
        numbers = numbers[:-1]
        for i in numbers :
            answer.append(i)
    else :
        temp = numbers[0]
        numbers = numbers[1:]
        for i in numbers :
            answer.append(i)
        answer.append(temp)
    return answer