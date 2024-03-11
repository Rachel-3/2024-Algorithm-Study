def solution(myString):
    answer = []
    split_x = myString.split("x")
    for i in split_x :
        if i != "" :
            answer.append(i)
    answer.sort()
    return answer