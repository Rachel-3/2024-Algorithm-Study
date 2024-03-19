def solution(num_list, n):
    answer = []

    for num in range(0, len(num_list), n):
        answer.append(num_list[num:num+n])

    return answer