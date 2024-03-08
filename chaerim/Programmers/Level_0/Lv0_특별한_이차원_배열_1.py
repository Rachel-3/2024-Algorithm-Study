def solution(n):
    answer = []

    for x in range(0, n):
        list = []
        for y in range(0, n):
            if x == y:
                list.append(1)
            else:
                list.append(0)
        answer.append(list)

    return answer