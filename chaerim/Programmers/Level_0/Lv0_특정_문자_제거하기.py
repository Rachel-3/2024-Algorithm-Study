def solution(my_string, letter):
    answer = ''

    for i in letter:
        my_string = my_string.replace(i,'')

    answer = my_string

    return answer