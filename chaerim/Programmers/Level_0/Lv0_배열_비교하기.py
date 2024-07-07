def solution(arr1, arr2):
    answer = 0

    arr1_len = len(arr1)
    arr2_len = len(arr2)

    if arr1_len > arr2_len:
        answer = 1
    elif arr1_len < arr2_len:
        answer = -1
    elif arr1_len == arr2_len:
        arr1_sum = sum(arr1)
        arr2_sum = sum(arr2)
        if arr1_sum > arr2_sum:
            answer = 1
        elif arr1_sum < arr2_sum:
            answer = -1
        elif arr1_sum == arr2_len:
            answer = 0

    return answer