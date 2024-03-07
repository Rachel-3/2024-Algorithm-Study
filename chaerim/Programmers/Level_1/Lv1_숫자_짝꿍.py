def solution(X, Y):
    answer = ''

    numbers = set(X) & set(Y)

    number = ''.join(min(X.count(partner), Y.count(partner)) * partner for partner in numbers)

    if number == '':
        answer = "-1"
    elif all(i == '0' for i in number):
        answer = "0"
    else:
        answer = ''.join(sorted(number, reverse=True))

    return answer