def solution(a, d, included):
    answer = a
    result = 0
    data = []
    for i in range(len(included)) :
        data.append(answer)
        answer += d
    for i in range(len(included)) :
        if included[i] == True :
            result += data[i]
    return result