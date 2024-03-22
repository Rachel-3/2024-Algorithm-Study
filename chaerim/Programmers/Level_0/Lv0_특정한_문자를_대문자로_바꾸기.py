def solution(my_string, alp):
    answer = ''

    alp_upper = alp.upper()
    answer = my_string.replace(alp, alp_upper)

    return answer