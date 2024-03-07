def solution(arr, queries):
    for query in queries:
        i, j = query
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr