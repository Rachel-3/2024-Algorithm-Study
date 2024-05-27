def solution(s):
    answer = 0

    bracket_dic = {')': '(', ']': '[', '}': '{'}
    for x in range(len(s)):
        rotation = s[x:] + s[:x]
        stack = []
        correct = True
        for bracket in rotation:
            if bracket in bracket_dic.values():
                stack.append(bracket)
            else:
                if not stack or stack.pop() != bracket_dic[bracket]:
                    correct = False
                    break
        if correct and not stack:
            answer += 1

    return answer