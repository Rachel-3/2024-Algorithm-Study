def solution(quiz):
    answer = []

    for i in quiz:
        if ' + ' in i:
            a, u = i.split(' + ')
            b, c = u.split(' = ')
            if int(a) + int(b) == int(c):
                answer.append('O')
            else:
                answer.append('X')
        elif ' - ' in i:
            a, u = i.split(' - ')
            b, c = u.split(' = ')
            if int(a) - int(b) == int(c):
                answer.append('O')
            else:
                answer.append('X')

    return answer