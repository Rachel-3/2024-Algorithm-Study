def solution(x1, x2, x3, x4):
    answer = True

    if x1 == True or x2 == True:
        x1_x2 = True
    else:
        x1_x2 = False

    if x3 == True or x4 == True:
        x3_x4 = True
    else:
        x3_x4 = False

    if x1_x2 == True and x3_x4 == True:
        answer = True
    else:
        answer = False

    return answer