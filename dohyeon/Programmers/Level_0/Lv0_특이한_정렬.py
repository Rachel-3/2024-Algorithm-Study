
def solution(numlist, n):
    answer = []
    for i in numlist:
        answer.append(i - n)
    
    result = []
    for i in sorted(answer[:], key=lambda x:[abs(x), -x]): 
        result.append(numlist[answer.index(i)])

    return result