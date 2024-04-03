def solution(common):
    answer = 0
    diff = common[1] - common[0]
    next_diff = common[-1] - common[-2]
    if diff == next_diff :
        answer = common[-1] + next_diff
    else :
        answer = common[-1] * (common[1] / common[0])
    return answer