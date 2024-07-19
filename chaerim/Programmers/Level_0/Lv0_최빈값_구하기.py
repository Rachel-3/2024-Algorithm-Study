def solution(array):
    answer = 0

    array_dic = {}

    for i in array:
        if i in array_dic:
            array_dic[i] += 1
        else:
            array_dic[i] = 1

    max_num = 0
    mult = False

    for key, value in array_dic.items():
        if value > max_num:
            max_num = value
            answer = key
            mult = False
        elif value == max_num:
            mult = True

    if mult:
        answer = -1

    return answer