def solution(s):
    answer = 0
    stack = []

    string_list = s.split()
    
    for i in string_list:
        if i == 'Z':
            if stack:
                last_num = stack.pop()
                answer -= last_num
        else:
            number = int(i)
            stack.append(number)
            answer += number

    return answer