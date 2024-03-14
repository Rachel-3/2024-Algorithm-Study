def solution(q, r, code):
    answer = ''
    for index, value in enumerate(list(code)) :
        if index % q == r :
            answer += value
    return answer