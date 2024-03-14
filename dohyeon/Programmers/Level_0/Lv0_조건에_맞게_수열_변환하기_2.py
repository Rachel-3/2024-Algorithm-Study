def solution(arr):
    answer = 0
    previous = []
    while True :
        previous = arr.copy()
        for i in range(len(arr)) :
            if arr[i] >= 50 and arr[i] % 2 == 0 :
                arr[i] /= 2
            elif arr[i] < 50 and arr[i] % 2 == 1 :
                arr[i] = (arr[i] * 2) + 1
        if arr == previous :
            break
        else :
            answer += 1

    return answer