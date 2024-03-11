def solution(number):
    answer = 0
    number = int(number)

    if number != 0:
        answer = number % ((number // 9) * 9)
    
    return answer