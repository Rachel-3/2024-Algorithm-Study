def solution(my_string, is_suffix):
    answer = 0

    string = []
    for i in range(0, len(my_string)):
        string.append(my_string[i:])
    
    if is_suffix in string:
        answer = 1
    else:
        answer = 0

    return answer