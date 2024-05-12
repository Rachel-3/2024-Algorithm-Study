def solution(my_strings, parts):
    answer = ''

    for i in range(len(my_strings)):
        my_string = my_strings[i]
        start, end = parts[i]
        answer += my_string[start:end + 1]

    return answer