from collections import Counter
def solution(k, tangerine):
    answer = 0
    k_list = (sorted(list(dict(Counter(tangerine)).values()), reverse = True))
    for i in range(0, len(k_list)) :
        k = k - k_list[i]
        if k <= 0 :
            answer = i + 1
            break
    return answer
