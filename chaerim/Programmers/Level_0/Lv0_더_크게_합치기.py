def solution(a, b):
    answer = 0

    word1 = int(str(a)+str(b))
    word2 = int(str(b)+str(a))

    if word1 >= word2:
        answer = word1
    else:
        answer = word2

    return answer