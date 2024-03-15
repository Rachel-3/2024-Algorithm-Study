def solution(picture, k):
    answer = []
    for i in picture :
        for j in range(k) :
            temp = ''
            for l in i :
                temp += l * k
            answer.append(temp)
    return answer