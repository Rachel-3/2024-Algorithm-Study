def solution(arr, query):
    answer = arr
    for index, value in enumerate(query) :
        if index % 2 == 0 :
            answer = answer[:value + 1]
        elif index % 2 == 1 :
            answer = answer[value:]
    return answer