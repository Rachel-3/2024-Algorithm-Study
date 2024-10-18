def solution(sizes):
    answer = 0

    max_size = max(max(size) for size in sizes)
    add_max_size = max(min(size) for size in sizes)

    answer = max_size * add_max_size

    return answer