def solution(myString):
    answer = []

    for string in myString.split('x'):
        if string:
            answer.append(string)

    answer.sort()

    return answer