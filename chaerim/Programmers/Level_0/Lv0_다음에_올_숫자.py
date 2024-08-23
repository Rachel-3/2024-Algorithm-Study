def solution(common):
    answer = 0

    l = []
    for i in range(1, len(common)):
        num = common[i] - common[i-1]
        if num not in l:
            l.append(num)

    if len(l) == 1:
        answer = common[-1] + l[0]
    else:
        ratio = common[1] // common[0]
        if all(common[i] // common[i-1] == ratio for i in range(1, len(common))):
            answer = common[-1] * ratio

    return answer