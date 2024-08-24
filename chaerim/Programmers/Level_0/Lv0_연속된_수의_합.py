def solution(num, total):
    answer = []

    start_num = (total - (num * (num - 1)) // 2) // num

    for i in range(num):
            answer.append(start_num + i)

    return answer