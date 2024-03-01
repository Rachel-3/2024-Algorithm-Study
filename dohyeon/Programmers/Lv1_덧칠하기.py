def solution(n, m, section):
    answer = 1
    part = section[0]
    for i in section :
        if part + (m - 1) < i :
            part = i
            answer += 1
            
    return answer