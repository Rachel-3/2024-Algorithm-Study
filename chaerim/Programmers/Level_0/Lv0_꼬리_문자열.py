def solution(str_list, ex):
    answer = ''

    for string in str_list:
        if ex not in string:
            answer += string

    return answer