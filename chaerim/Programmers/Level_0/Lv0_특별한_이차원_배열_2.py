def solution(arr):
    answer = 1

    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i][j] != arr[j][i]:
                answer = 0
                break

    return answer