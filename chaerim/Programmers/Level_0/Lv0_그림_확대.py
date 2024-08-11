def solution(picture, k):
    answer = []

    for i in picture:
        pic = ""
        for j in i:
            pic += j * k
        for _ in range(k):
            answer.append(pic)

    return answer