def solution(intStrs, k, s, l):
    answer = []

    
    for intStr in intStrs:
        string = intStr[s:s+l]
        if int(string) > k:
            answer.append(int(string))

    return answer