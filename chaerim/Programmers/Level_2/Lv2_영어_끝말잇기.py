def solution(n, words):
    answer = []

    word_list = []
    word_list.append(words[0])
    for i in range(1, len(words)):
        if words[i] in word_list or words[i][0] != words[i - 1][-1]:
            answer = [(i%n) + 1, (i//n) + 1]
            break
        word_list.append(words[i])

    if not answer:
        answer = [0, 0]

    return answer