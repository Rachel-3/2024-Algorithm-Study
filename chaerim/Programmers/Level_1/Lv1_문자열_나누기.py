def solution(s):
    answer = 0

    x = ''
    x_count = 0
    y_count = 0
    for i in s:
        if not x:
            x = i
            x_count = 1
        elif x and i == x:
            x_count += 1
        elif x and i != x:
            y_count += 1

        if x_count == y_count:
            answer += 1
            x = ''
            x_count = 0
            y_count = 0

    if x:
        answer += 1

    return answer