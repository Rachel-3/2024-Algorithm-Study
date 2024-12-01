# 백준 2003 - 수들의 합 2
# 분류 : 투포인터
N, M = map(int, input().split())
A = list(map(int, input().split()))

start, end = 0, 0
sum = 0
count = 0
while True :
    if sum >= M :
        sum -= A[start]
        start += 1
    elif end == N :
        break
    else :
        sum += A[end]
        end += 1
    if sum == M :
        count += 1
print(count)