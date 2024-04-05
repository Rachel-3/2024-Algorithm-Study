def solution(clothes):
    answer = 1

    clothes_dic = {}
    for cloth in clothes:
        if cloth[1] in clothes_dic:
            clothes_dic[cloth[1]] += 1
        else:
            clothes_dic[cloth[1]] = 2

    for count in clothes_dic.values():
        answer *= count

    answer -= 1

    return answer