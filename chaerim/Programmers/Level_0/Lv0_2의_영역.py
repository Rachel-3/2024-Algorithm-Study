def solution(arr):
    answer = []

    index = -1
    for i, num in enumerate(arr):
        if num == 2:
            if index == -1:
                answer.append(num)
                index = i
            else:
                answer = arr[index:i+1]

    if not answer:
        answer.append(-1)

    return answer