def solution(rank, attendance):
    answer = 0

    rank_list = []
    for i in range(len(rank)):
        if attendance[i] == True:
            rank_list.append(rank[i])

    rank_list.sort()

    for i in range(3):
        a = rank.index(rank_list[i])
        if i == 0:
            answer += a * 10000
        elif i == 1:
            answer += a * 100
        else:
            answer += a

    return answer