def solution(name, yearning, photo):
    answer = []

    for i in range(len(photo)):
        score = 0
        for people in range(len(name)):
            if name[people] in photo[i]:
                score += yearning[people]
        answer.append(score)
            
    return answer