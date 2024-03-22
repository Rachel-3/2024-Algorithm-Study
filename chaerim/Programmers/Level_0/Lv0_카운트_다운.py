def solution(start, end_num):
    answer = []

    for i in range(start, -1, -1):
        if i != end_num:
            answer.append(i)
        else:
            answer.append(i)
            break

    return answer