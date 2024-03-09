def solution(my_string, s, e):
    answer = ''

    for i in range(0, s):
        answer += my_string[i]

    string = ''
    for i in range(s, e+1):
        string += my_string[i]
    
    answer += string[-1::-1]

    for i in range(e+1, len(my_string)):
        answer += my_string[i]

    return answer