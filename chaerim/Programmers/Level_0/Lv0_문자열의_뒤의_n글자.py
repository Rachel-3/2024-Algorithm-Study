def solution(my_string, n):
    answer = ''

    string = my_string[-1::-1]

    for i in range(0, n):
        answer += string[i]

    answer = answer[-1::-1]
    
    return answer