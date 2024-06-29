def solution(numbers):
    answer = ''

    num_list = list(map(str, numbers))

    num_list.sort(key=lambda x: x*3, reverse=True)
    
    if num_list[0] == '0':
        answer = '0'
    else:
        answer = ''.join(num_list)

    return answer