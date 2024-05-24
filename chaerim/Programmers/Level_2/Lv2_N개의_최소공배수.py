def solution(arr):
    answer = 0

    progress = arr[0]
    for num in arr[1:]:
        mul = progress * num

        while num:
            progress, num = num, progress % num
        progress = mul // progress

    answer = progress

    return answer