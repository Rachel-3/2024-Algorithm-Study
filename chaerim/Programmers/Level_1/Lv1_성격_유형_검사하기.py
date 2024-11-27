def solution(survey, choices):
    answer = ''

    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        question = survey[i]
        choice = choices[i]
        score = abs(choice - 4)

        if choice < 4:
            scores[question[0]] += score
        elif choice > 4:
            scores[question[1]] += score
        
    answer += 'R' if scores['R'] >= scores['T'] else 'T'
    answer += 'C' if scores['C'] >= scores['F'] else 'F'
    answer += 'J' if scores['J'] >= scores['M'] else 'M'
    answer += 'A' if scores['A'] >= scores['N'] else 'N'

    return answer