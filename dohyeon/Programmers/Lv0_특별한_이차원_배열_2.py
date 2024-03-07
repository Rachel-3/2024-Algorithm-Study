def solution(arr) :
    answer = 1
    for i in range(len(arr)) :
        for j in range(len(arr[i])) :
            if arr[i][j] != arr[j][i] : return 0
    return answer

print(solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]])) # 1