def solution(myStr):
    answer = []

    word = ''
    for char in myStr:
        if char not in ['a', 'b', 'c']:
            word += char
        else:
            if word != '':
                answer.append(word)
                word = ''

    if answer or word != '':
        answer.append(word)
    else:
        answer.append("EMPTY")

    return answer