def solution(n, lost, reserve):
    answer = 0

    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    for i in reserve_set:
        if i - 1 in lost_set:
            lost_set.remove(i - 1)
        elif i + 1 in lost_set:
            lost_set.remove(i + 1)

    answer = n - len(lost_set)

    return answer