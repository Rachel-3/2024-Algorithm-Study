def solution(numbers, k):
    answer = []
    start = 1
    for i in range(k) :
        start += 2
        if start > len(numbers) :
            start -= len(numbers)
        answer.append(start)
    return answer[-2]