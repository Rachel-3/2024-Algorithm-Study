def solution(str_list):
    answer = []

    for i, string in enumerate(str_list):
        if string == 'l':
            answer = str_list[:i]
            break
        elif string == 'r':
            answer = str_list[i+1:]
            break

    return answer