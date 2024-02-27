def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    sliced_lists = [score[i:i+m] for i in range(0, len(score), m)]
    for i in sliced_lists :
        if len(i) == m :
            answer += min(i) * m
    
    return answer