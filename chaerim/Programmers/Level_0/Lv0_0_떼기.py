def solution(n_str):
    answer = ''

    i = 0
    while i == 0:
        if n_str[i] == '0':
            n_str = n_str[:i] + n_str[i+1:]
        else:
            break
    
    answer = n_str

    return answer