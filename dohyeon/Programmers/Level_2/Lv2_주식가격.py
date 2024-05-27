def solution(prices):
    answer = []
    for i in range(len(prices)) :
        temp = 0
        for j in range(i, len(prices)) : 
            if prices[i] <= prices[j] :
                temp += 1
            else :
                temp += 1
                break
        answer.append(temp - 1)
    return answer