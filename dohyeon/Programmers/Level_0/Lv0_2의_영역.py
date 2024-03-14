def solution(arr):
    answer = []
    if 2 not in arr :
        return [-1]
    else :
        answer = arr[[i for i, value in enumerate(arr) if value == 2][0] : [i for i, value in enumerate(arr) if value == 2][-1] + 1]
    return answer