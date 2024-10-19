def solution(s):
    answer = []

    t = ''
    for i in s:
        if i not in t:
            answer.append(-1)
        else:
            len_t = len(t)
            index = t.rfind(i)
            answer.append(len_t - index)
        t += i

    return answer