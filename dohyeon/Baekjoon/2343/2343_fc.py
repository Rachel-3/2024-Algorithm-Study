n, m = map(int, input().split())
running_time = list(map(int, input().split()))

left = max(running_time)
right = sum(running_time)

answer = 0

while left <= right :
    middle = (left + right) // 2

    blueray_num =1 
    remain = middle
    for i in range(n) :
        if remain < running_time[i] :
            blueray_num += 1
            remain = middle

        remain -= running_time[i]
    
    if blueray_num <= m :
        answer = middle
        right = middle - 1
    else :
        left = middle + 1

print(answer)