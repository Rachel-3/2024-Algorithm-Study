def solution(my_string, indices):
    answer = ''

    for index, char in enumerate(my_string):
        if index not in indices:
            answer += char

    return answer