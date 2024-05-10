def solution(my_string):
    answer = 0

    for string in my_string:
        if string.isdigit():
            answer += int(string)
        
    return answer