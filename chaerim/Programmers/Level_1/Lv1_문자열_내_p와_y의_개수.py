def solution(s):
    answer = True
    
    s = s.lower()

    if s.count('p') == s.count('y'):
        answer = True
    else:
        answer = False

    return answer