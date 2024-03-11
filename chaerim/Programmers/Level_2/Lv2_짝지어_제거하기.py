def solution(s):
    answer = 0

    list = []
    for char in s:
        if not list or list[-1] != char:
            list.append(char)
        else:
            list.pop()

    if not list:
        answer = 1

    return answer