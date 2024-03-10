def solution(numLog):
    answer = ''

    for i in range(0, len(numLog) - 1):
        difference = int(numLog[i+1]) - int(numLog[i])
        if difference == 1:
            answer += "w"
        elif difference == -1:
            answer += "s"
        elif difference == 10:
            answer += "d"
        elif difference == -10:
            answer += "a"

    return answer