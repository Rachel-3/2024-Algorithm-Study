def solution(s):
    answer = ''
    for i in s.split(" ") :
        try : answer += i[0].upper()
        except : pass
        answer += i[1:].lower()
        answer += " "
    return answer[:-1]