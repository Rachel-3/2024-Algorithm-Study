def solution(score):
    answer = []

    average = []
    for grade in score:
        average.append(sum(grade)/2)

    sorted_average = sorted(average, reverse=True)

    for avg in average:
        answer.append(sorted_average.index(avg) + 1)

    return answer