n = int(input())
budget = list(map(int, input().split(" ")))
max_budget = int(input())

left, right = 0, max(budget)

while left <= right :
    middle = (left + right) // 2
    sum = 0
    for i in range(n) :
        sum += min(middle, budget[i])
    
    if sum <= max_budget :
        answer = middle
        left = middle + 1
    else :
        right = middle - 1

print(answer)