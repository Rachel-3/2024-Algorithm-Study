def solution(arr, queries):
    for i in range(len(queries)) :
        s, e = queries[i]
        for j in range(s, e + 1) :
            arr[j] += 1
    return arr