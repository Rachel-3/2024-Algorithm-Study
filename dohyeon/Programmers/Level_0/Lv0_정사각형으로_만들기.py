def solution(arr):
    answer = []
    x, y = len(arr), len(arr[0])
    length = max(x, y)
    for i in range(length) :
        temp = []
        for j in range(length) :
            try :
                temp.append(arr[i][j])
            except :
                temp.append(0)
        answer.append(temp)
    return answer