def solution(sequence, k):
    answer = []

    start = 0
    sequence_sum = 0
    for end in range(len(sequence)):
        sequence_sum += sequence[end]

        while sequence_sum > k:
            sequence_sum -= sequence[start]
            start += 1

        if sequence_sum == k:
            sort_length = end - start
            if not answer:
                answer = [start, end]
            elif sort_length < answer[1] - answer[0]:
                answer = [start, end]

    return answer