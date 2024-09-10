def solution(seoul):
    answer = '김서방은 x에 있다'

    kim_index = 0
    for index, string in enumerate(seoul):
        if string == 'Kim':
            kim_index = index

    answer = answer.replace('x', str(kim_index))

    return answer