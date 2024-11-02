def solution(s):
    answer = ''

    s_count = {}

    for char in s:
        if char in s_count:
            s_count[char] += 1
        else:
            s_count[char] = 1
    
    one_char = [char for char in s_count if s_count[char] == 1]

    one_char.sort()

    answer = ''.join(one_char)

    return answer