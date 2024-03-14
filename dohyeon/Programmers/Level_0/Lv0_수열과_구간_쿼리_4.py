def solution(arr, queries):
    answer = []
    for i in range(len(queries)) :
        s = queries[i][0]
        e = queries[i][1]
        k = queries[i][2]
        for j in range(s, e + 1) :
            if j % k == 0 :
                arr[j] += 1
    return arr