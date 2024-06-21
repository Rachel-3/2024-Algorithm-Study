def solution(num_list):
    comb = 1
    multi = 0

    for i in num_list:
        comb *= i
        multi += i
    
    multi = multi**2
    if comb < multi:
        answer = 1
    else:
        answer = 0

    return answer