def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for p_name, c_name in zip(participant, completion):
        if p_name != c_name:
            return p_name

    return participant[-1]