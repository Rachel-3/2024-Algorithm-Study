def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero = lottos.count(0)

    win = 0
    for i in lottos:
        if i in win_nums:
            win += 1

    max_rank = rank[win + zero]
    min_rank = rank[win]

    answer = [max_rank, min_rank]

    return answer