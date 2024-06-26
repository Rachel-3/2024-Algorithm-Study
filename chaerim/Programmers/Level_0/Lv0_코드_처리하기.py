def solution(code):
    ret = ''
    mode = 0

    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != "1":
                if idx%2 == 0:
                    ret += code[idx]
            else:
                mode = 1
        else:
            if code[idx] != "1":
                if idx%2 != 0:
                    ret += code[idx]
            else:
                mode = 0

    answer = ret if ret else "EMPTY"

    return answer