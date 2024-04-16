def solution(numbers):
    answer = 0
    
    for i in numbers:
        answer += i

    answer = answer/len(numbers)

    return answer