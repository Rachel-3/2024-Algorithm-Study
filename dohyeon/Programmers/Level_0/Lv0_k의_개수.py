def solution(i, j, k):
    answer = 0
    for index in range(i, j + 1) :
        answer += (str(index).count(str(k)))
    return answer