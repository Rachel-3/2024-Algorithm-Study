def solution(arr, flag):
    answer = []

    for index, fl in enumerate(flag):
        if fl == True:
            answer.extend([arr[index]] * (arr[index] * 2))
        else:
            answer = answer[:-arr[index]]

    return answer