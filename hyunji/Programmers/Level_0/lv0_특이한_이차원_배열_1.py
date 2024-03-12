def solution(n):
    arr = [[0 for j in range(n)] for i in range(n)]
    for k in range(n):
        arr[k][k] = 1
    answer = arr
    return answer