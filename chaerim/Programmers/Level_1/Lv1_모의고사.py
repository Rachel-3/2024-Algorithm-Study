def solution(answers):
    answer = []

    person_1 = [1, 2, 3, 4, 5]
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    success = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == person_1[i % len(person_1)]:
            success[0] += 1
        if answers[i] == person_2[i % len(person_2)]:
            success[1] += 1
        if answers[i] == person_3[i % len(person_3)]:
            success[2] += 1

    max_score = max(success)
    for index, score in enumerate(success):
        if score == max_score:
            answer.append(index + 1)

    return answer