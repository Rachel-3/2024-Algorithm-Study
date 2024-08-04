def solution(arr, query):
    answer = []

    for i, num in enumerate(query):
        if i%2 == 0:
            arr = arr[:num+1]
        else:
            arr = arr[num:]

    answer = arr

    return answer