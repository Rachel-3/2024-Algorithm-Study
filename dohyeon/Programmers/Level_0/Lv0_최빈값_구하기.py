def solution(array):
    array_dict = {}
    for i in array :
        if str(i) in array_dict :
            array_dict[str(i)] += 1
        else :
            array_dict[str(i)] = 1
    max_ = [k for k,v in array_dict.items() if max(array_dict.values()) == v]
    if len(max_) != 1 :
        return -1
    else :
        return int(max_[0])