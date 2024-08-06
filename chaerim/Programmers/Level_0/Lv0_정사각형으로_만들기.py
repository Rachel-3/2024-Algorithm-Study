def solution(arr):
    answer = [[]]

    arr_column = len(arr)
    arr_row = len(arr[0])

    if arr_column == arr_row:
        return arr
    elif arr_column > arr_row:
        zero_count = arr_column - arr_row
        for row in arr:
            row.extend([0] * zero_count)
    else:
        zero_count = arr_row - arr_column
        for _ in range(zero_count):
            arr.append([0] * arr_row)

    answer = arr

    return answer