def solution(num_list):
    answer = 0
    for i in num_list :
        while i > 1 :
            if i == 1 : break
            else :
                i //= 2
                answer += 1
    return answer