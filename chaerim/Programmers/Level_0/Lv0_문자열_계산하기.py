def solution(my_string):
    answer = 0
    stack = []

    string_list = my_string.split()
    
    for i in string_list:
        if i == '+' or i == '-':
            stack.append(i)
        else:
            number = int(i)

            if stack and stack[-1] == '+':
                answer += number
                stack.pop()
            elif stack and stack[-1] == '-':
                answer -= number
                stack.pop()
            else:
                answer += number

    return answer