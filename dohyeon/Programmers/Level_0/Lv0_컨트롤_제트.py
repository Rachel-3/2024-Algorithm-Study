def solution(s):
    stack = []
    s = s.split(" ")
    for i in s :
        if i == "Z" :
            stack.pop()
        else :
            stack.append(i)
    stack = map(int, stack)
    return sum(stack)