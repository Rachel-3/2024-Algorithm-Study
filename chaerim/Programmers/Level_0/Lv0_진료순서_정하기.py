def solution(emergency):
    answer = [0] * len(emergency)

    start = 1
    while start <= len(emergency):
        num_max = max(emergency)
        max_index = emergency.index(num_max)
        answer[max_index] = start
        emergency[max_index] = -1
        start += 1

    return answer