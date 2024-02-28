def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)

    score_list = []
    for i in range(0, len(score), m):
        score_list.append(score[i:i+m])

    for i in score_list:
        if len(i) == m:
            answer += min(i) * m

    return answer