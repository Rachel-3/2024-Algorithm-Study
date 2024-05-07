from collections import Counter

def solution(topping) :
    answer = 0
    dic = Counter(topping)
    exist_values = set()
    
    for i in topping :
        dic[i] -= 1
        exist_values.add(i)
        if dic[i] == 0 :
            dic.pop(i)
        if len(dic) == len(exist_values) :
            answer += 1
    return answer