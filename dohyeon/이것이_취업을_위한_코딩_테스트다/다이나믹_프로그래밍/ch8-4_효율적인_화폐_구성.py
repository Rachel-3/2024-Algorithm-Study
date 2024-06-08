n, m = list(map(int, input().split()))
datas = []
for i in range(n) :
    datas.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n) :
    for j in range(datas[i], m + 1) :
        if d[j - datas[i]] != 10001 :
            d[j] = min(d[j], d[j - datas[i]] + 1)

if d[m] == 10001 :
    print(-1)
else :
    print(d[m])