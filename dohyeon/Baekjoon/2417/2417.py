# 백준 2417 - 정수 제곱근

n = int(input())

low = 0
high = 2 ** 32

ans = -1
while low <= high :
    mid = (low + high) // 2
    if mid ** 2 < n :
        low = mid + 1
    else :
        ans = mid
        high = mid - 1

print(ans)
