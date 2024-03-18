def solution(score):
    answer = []
    avg_score = []
    for i in score :
        avg_score.append((i[0] + i[1]) / 2)
    ranks = [sorted(avg_score, reverse=True).index(ele) for ele in avg_score]
    for i in ranks :
        answer.append(i + 1)
    return answer