def solution(num_list):
    answer = []

    if num_list[-1] > num_list[-2]:
        i = num_list[-1] - num_list[-2]
        num_list.append(i)
    else:
        i = 2 * num_list[-1]
        num_list.append(i)

    answer = num_list
    
    return answer