n, m = list(map(int, input().split()))

datas = list(map(int, input().split()))

start = 0
end = max(datas)

result = 0
while start <= end :
    mid = (start + end) // 2
    total = 0
    for i in datas :
        # 잘랐을때 떡의 양 계산
        if i > mid :
            total += i - mid
    # 잘린 떡의 양이 필요한 양보다 작은 경우 왼쪽 부분 탐색, 더 많이 잘라야함
    if total < m :
        end = mid - 1
    # 떡의 양이 충분하다면 덜 자르기, 오른쪽 부분 탐색
    else :
        result = mid
        start = mid + 1
print(result)