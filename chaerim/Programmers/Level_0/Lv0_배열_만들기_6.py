def solution(arr):
    answer = []
    
    arr_len = len(arr)
    i = 0
    while i < arr_len:
        if not answer:
            answer.append(arr[i])
            i += 1
        elif len(answer) > 0 and answer[-1] == arr[i]:
            answer.pop()
            i += 1
        elif len(answer) > 0 and answer[-1] != arr[i]:
            answer.append(arr[i])
            i += 1

    if not answer:
        answer.append(-1)

    return answer