def solution(lines):
    answer = 0

    min_start = min(line[0] for line in lines)
    max_end = max(line[1] for line in lines)

    length = [0] * (max_end - min_start)

    for line in lines:
        start, end = line
        for i in range(start, end):
            length[i - min_start] += 1

    answer = sum(1 for x in length if x > 1)

    return answer