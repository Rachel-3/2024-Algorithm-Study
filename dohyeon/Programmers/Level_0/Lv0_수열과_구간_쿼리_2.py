def solution(arr, queries):
    answer = []
    for i in queries :
        s, e, k = i[0], i[1], i[2]
        temp = []
        for j in range(s, e + 1) :
            if arr[j] > k :
                temp.append(arr[j])
        if temp != [] :
            answer.append(min(temp))
        else :
            answer.append(-1)
    return answer