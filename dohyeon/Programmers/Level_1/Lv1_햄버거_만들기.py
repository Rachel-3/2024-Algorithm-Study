def solution(ingredient) :
    answer = 0
    stack = []
    make_step = [1, 2, 3, 1]
    for i in range(len(ingredient)) :
        stack.append(ingredient[i])
        if stack[-4:] == make_step :
            answer += 1
            for j in range(4) :
                stack.pop()  
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1])) # 2
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2])) # 0