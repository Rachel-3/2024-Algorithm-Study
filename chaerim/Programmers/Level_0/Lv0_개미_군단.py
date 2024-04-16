def solution(hp):
    answer = 0

    general_ant = hp // 5
    hp = hp - (general_ant * 5)
    soldier_ant = hp // 3
    worker_ant = hp % 3

    answer = general_ant + soldier_ant + worker_ant

    return answer