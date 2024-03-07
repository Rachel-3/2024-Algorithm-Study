def solution(arr1, arr2):
    answer = 0
    if len(arr1) != len(arr2) :
        if len(arr1) > len(arr2) : answer = 1
        else : answer = -1
    else :
        sum_arr1 = sum(arr1)
        sum_arr2 = sum(arr2)
        if sum_arr1 > sum_arr2 : answer = 1
        elif sum_arr1 < sum_arr2 : answer = -1
        else : answer = 0
    return answer