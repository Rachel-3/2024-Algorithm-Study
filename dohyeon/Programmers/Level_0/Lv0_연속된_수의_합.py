def solution(num, total):
    result = 0
    for i in range(1, num):
        result += i
    start = (total - result) // num
    answer = [i for i in range(start, start + num)]
    return answer