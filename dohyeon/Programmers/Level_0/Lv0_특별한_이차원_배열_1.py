def solution(n) :
    answer =[]
    for i in range(n) :
        sub_list = []
        for j in range(n) :
            if i == j :
                sub_list.append(1)
            else :
                sub_list.append(0)
        answer.append(sub_list)
    return answer

print(solution(3)) # [[1, 0, 0], [0, 1, 0], [0, 0, 1]]