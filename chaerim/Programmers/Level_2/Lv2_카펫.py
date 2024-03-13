def solution(brown, yellow):
    answer = []
    found = False

    for x in range(1, int(brown/2)+1):
        if found:
            break
        for y in range(1, int(brown/2)+1):
            if 2*(x+y)-4 == brown:
                if brown+yellow == x*y:
                    answer.append(x)
                    answer.append(y)
                    found = True

    answer.sort(reverse=True)

    return answer