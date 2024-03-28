def check_bracket(s) :
    dic = {')' : '(', ']' : '[', '}': '{'}
    stack = []
    for char in s:
        if (char in '({['):
            stack.append(char)
        else:
            if (stack):
                top = stack.pop()
                if (dic[char] != top):
                    return False
            else:
                return False
    return True
        
def solution(s):
    answer = 0
    if len(s) % 2 == 1 :
        return 0
    for i in range(len(s)) :
        s = s[-1] + s[0 : -1]
        if check_bracket(s) :
            answer += 1
    return answer