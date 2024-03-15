def solution(num_list):
    answer = [0]*2

    for num in num_list:
        if num%2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1

    return answer