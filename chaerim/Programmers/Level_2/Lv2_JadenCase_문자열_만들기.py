def solution(s):
    answer = ''

    s_list = []
    for i in range(len((s))):
        if i == 0 or s[i - 1] == ' ':
            s_list.append(s[i].upper())
        else:
            s_list.append(s[i].lower())

    answer = ''.join(s_list)

    return answer