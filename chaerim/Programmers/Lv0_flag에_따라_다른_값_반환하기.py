def solution(a, b, flag):
    answer = 0

    flag = str(flag)

    if flag == "True":
        answer += a + b
    else:
        answer += a - b

    return answer