# 백준 10810 - 공 넣기

N, M = map(int, input().split())
baskets = {}
for i in range(1, N + 1) :
    baskets[i] = 0
for _ in range(M) :
    a, b, c = map(int, input().split())
    for i in range(a, b + 1) :
        baskets[i] = c
for i in list(baskets.values()) :
    print(i, end = " ")