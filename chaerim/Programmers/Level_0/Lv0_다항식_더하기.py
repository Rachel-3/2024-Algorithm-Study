def solution(polynomial):
    answer = ''
    polynomial = polynomial.split(" + ")

    num_count = 0
    x_count = 0
    for term in polynomial:
        if 'x' in term:
            if term == 'x':
                x_count += 1
            else:
                x_count += int(term[:-1])
        else:
            num_count += int(term)
    
    if num_count == 0:
        answer = str(x_count) + 'x'
        if x_count == 1:
            answer = 'x'
    elif x_count == 0:
        answer = str(num_count)
    elif x_count == 1:
        answer = 'x + ' + str(num_count)
    else:
        answer = str(x_count) + 'x + ' + str(num_count)

    return answer