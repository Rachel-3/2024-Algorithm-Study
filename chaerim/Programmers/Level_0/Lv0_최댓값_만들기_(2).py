def solution(numbers):
    answer = 0

    list = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            mul = numbers[i] * numbers[j]
            list.append(mul)
    
    answer = max(list)

    return answer