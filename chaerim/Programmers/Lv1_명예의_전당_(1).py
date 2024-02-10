def solution(k, score):
    answer = []
    rank_score = []

    for r in score:
        if len(rank_score) < k:
            rank_score.append(r)
            rank_score.sort(reverse=True)
        else:
            if r > rank_score[-1]:
                rank_score.pop()
                rank_score.append(r)
                rank_score.sort(reverse=True)

        answer.append(rank_score[-1])

    return answer