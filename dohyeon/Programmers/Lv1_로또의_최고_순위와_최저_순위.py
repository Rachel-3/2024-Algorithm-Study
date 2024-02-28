def solution(lottos, win_nums):
    answer = [0, 0]
    min_rank = 0
    for i in lottos :
        if i in win_nums :
            min_rank += 1
    zero_count = 0
    for i in lottos : 
        if i == 0 :
            zero_count += 1
    if min_rank == 6 : answer[1] = 1
    elif min_rank == 5: answer[1] = 2
    elif min_rank == 4 : answer[1] = 3
    elif min_rank == 3 : answer[1] = 4
    elif min_rank == 2 : answer[1] = 5
    else : answer[1] = 6
    temp = (answer[1] - zero_count)
    if temp <= 0 : temp = 1
    answer[0] = temp
    return answer