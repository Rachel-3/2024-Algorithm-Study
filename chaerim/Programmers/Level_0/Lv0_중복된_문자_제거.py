def solution(my_string):
    answer = ''

    for char in my_string:
        if char not in answer:
            answer += char

    return answer