def solution(elements):
    answer = 0

    elements_len = len(elements)
    total_sum = set()

    for i in range(elements_len):
        total = 0
        for j in range(elements_len):
            total += elements[(i + j) % elements_len]
            total_sum.add(total)

    answer = len(total_sum)

    return answer