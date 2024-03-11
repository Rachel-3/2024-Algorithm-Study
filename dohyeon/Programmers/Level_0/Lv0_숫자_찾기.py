def solution(num, k):
    answer = -1
    num = str(num)
    for idx, value in enumerate(str(num)) :
        if str(k) == value :
            answer = idx + 1
            break
    return answer