def solution(arr):
    answer = []

    if len(arr) == 1:
        answer.append(-1)
    else:
        min_arr = min(arr)
        min_arr_index = arr.index(min_arr)
        answer = arr[:min_arr_index] + arr[min_arr_index + 1:]

    return answer