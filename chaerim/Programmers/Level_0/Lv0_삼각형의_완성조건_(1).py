def solution(sides):
    answer = 0

    max_side = max(sides)
    sum_side = sum(sides) - max_side

    if max_side >= sum_side:
        answer = 2
    else:
        answer = 1

    return answer