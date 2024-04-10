def solution(s):
    answer = ''

    s_split = list(map(int, s.split(' ')))

    answer += str(min(s_split)) + ' ' + str(max(s_split))

    return answer