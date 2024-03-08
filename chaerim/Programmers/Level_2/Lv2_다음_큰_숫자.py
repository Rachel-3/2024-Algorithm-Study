def solution(n):
    answer = 0

    num_count = bin(n).count('1')

    while True:
        n += 1
        next_count = bin(n).count('1')

        if next_count == num_count:
            answer = n
            break

    return answer