def solution(myString, pat):
    answer = 0

    pat_len = len(pat)
    for i in range(0, len(myString)):
        if pat in myString[i:i+pat_len]:
            answer += 1

    return answer