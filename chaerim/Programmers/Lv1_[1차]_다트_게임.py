def solution(dartResult):
    dartResult = dartResult.replace('10', 'A')
    score = []

    for i in dartResult:
        if i.isnumeric():
            temp = int(i)
        elif i == 'A':
            temp = 10
        elif i == 'S':
            score.append(temp**1)
        elif i == 'D':
            score.append(temp**2)
        elif i == 'T':
            score.append(temp**3)
        elif i == '*':
            score[-1] *= 2
            if len(score) >= 2:
                score[-2] *= 2
        elif i == '#':
            score[-1] *= -1

    answer = sum(score)

    return answer