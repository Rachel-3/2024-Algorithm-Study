def solution(land):
    answer = 0
    index = 0
    for i in range(len(land)) :
        # if i != 0 :
        #     del land[i][index]
        index = land[i].index(max([land[i]]))
        answer += max(land[i])

    return answer
print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))