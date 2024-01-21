def solution(numbers, target):
    answer = 0
    q = [[numbers[0], 0], [-1 * numbers[0], 0]]
    while q :
        temp, i = q.pop()
        i += 1
        if i < len(numbers) :
            q.append([temp + numbers[i], i])
            q.append([temp - numbers[i], i])
        else :
            if temp == target :
                answer += 1
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))