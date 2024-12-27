n, m = map(int, input().split())
lessons = list(map(int, input().split()))

start = max(lessons)
end = sum(lessons)
count = 0
while start <= end :
    mid = (start + end) // 2
    sum = 0
    blueray = 1
    for lesson in lessons :
        if sum + lesson > mid :
            blueray += 1
            sum = 0
        sum += lesson
    if blueray <= m :
        end = mid - 1
    else :
        start = mid + 1
print(start)