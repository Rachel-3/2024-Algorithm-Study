'''
채점 결과
정확성: 44.1
합계: 44.1 / 100.0

def solution(sequence, k):
    answer = []
    start = 0
    while start < k :
        new_list = sequence[start:]
        if k in new_list :
            return [new_list.index(k), new_list.index(k)]
        value = 0
        for i in range(len(new_list)) :
            value += new_list[i]
            if value > k :
                break
            elif value == k :
                return [start, start + i]
        start += 1
        
    return answer
'''

def solution(sequence, k):
    start, end = 0, 0
    current_sum = sequence[0]
    min_length = float('inf')
    answer = [-1, -1]
    
    while end < len(sequence):
        if current_sum == k:
            if (end - start) < min_length:
                min_length = end - start
                answer = [start, end]
            current_sum -= sequence[start]
            start += 1
        elif current_sum < k:
            end += 1
            if end < len(sequence):
                current_sum += sequence[end]
        else:
            current_sum -= sequence[start]
            start += 1

    return answer