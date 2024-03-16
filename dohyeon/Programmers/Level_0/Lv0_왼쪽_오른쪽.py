def solution(str_list):
    check = 0
    for i in range(len(str_list)) :
        if str_list[i] == "l" :
            check = 1
            return str_list[:i]
        elif str_list[i] == "r" :
            check = 1
            return str_list[i + 1:]
    if check == 0 :
        return []