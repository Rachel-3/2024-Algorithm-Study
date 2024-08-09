def solution(my_string):
    answer = ''

    for i in my_string:
        if i.islower():
            answer += i.upper()
        elif i.isupper():
            answer += i.lower()

    return answer