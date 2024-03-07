def solution(dartResult):
    answer = 0
    stack = []
    dartResult = dartResult.replace("10", "k")
    for i in dartResult :
        if i.isnumeric() :
            answer += int(i)
            continue
        elif  i == "k" :
            answer += 10
            continue
        elif i == 'S' :
            stack.append(answer)
        elif i == 'D' :
            stack.append(answer ** 2)
        elif i == 'T' :
            stack.append(answer ** 3)
        elif i == "*" : # 스타상
            if len(stack) >= 2 :
                stack[-1] = stack[-1] * 2
                stack[-2] = stack[-2] * 2
            else :
                stack[-1] = stack[-1] * 2
        elif i == "#" : # 아차상
            stack[-1] = stack[-1] * -1
        answer = 0
            
            
    return sum(stack)