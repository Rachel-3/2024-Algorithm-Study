def solution(num_list):
    answer = 0
    for i in num_list:
        if i < 0:
            answer = num_list.index(i)
            break
        else:
            answer = -1
    return answer