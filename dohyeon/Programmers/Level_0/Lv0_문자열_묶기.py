def solution(strArr):
    answer = 0
    dict = {}
    for i in strArr :
        if str(len(i)) in dict :
            dict[str(len(i))] += 1
        else :
            dict[str(len(i))] = 1
    return max(([value for key, value in dict.items()]))