def solution(myString, pat):
    answer = 0
    first = 0
    while True :
        index = myString.find(pat, first)
        if index == -1 :
            break
        answer += 1
        first = index + 1
    return answer