def solution(k, score):
    answer = []
    temp = []
    for i in range(len(score)) :
        if len(temp) < k :
            temp.append(score[i])
        else :
            if min(temp) < score[i] :
                temp.remove(min(temp))
                temp.append(score[i])
        answer.append(min(temp))
    return answer

k1 = 3
score1 = [10, 100, 20, 150, 1, 100, 200]
result1 = [10, 10, 10, 20, 20, 100, 100]

k2 = 4
score2 = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
result2 = [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]

print(solution(k1, score1) == result1)
print(solution(k2, score2) == result2)