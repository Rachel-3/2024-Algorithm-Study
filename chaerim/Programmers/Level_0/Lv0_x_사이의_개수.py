def solution(myString):
    answer = []

    myString = myString.split('x')

    for char in myString:
        answer.append(len(char))

    return answer