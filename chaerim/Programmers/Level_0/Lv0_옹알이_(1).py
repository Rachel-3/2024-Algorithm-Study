def solution(babbling):
    answer = 0
    talk = ["aya", "ye", "woo", "ma"]

    for i in babbling:
        temp = i
        for p in talk:
            temp = temp.replace(p, '.')

        if temp.replace('.', '') == '':
            answer += 1

    return answer