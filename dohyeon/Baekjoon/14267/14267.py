# 백준 14267 - 회사 문화 1
# 분류 : 트리

n, m = list(map(int, input().split()))
parent = list(map(int, input().split()))

for i in range(1, n) :
    parent[i] -= 1

good = [0] * n
for _ in range(m) :
    id, score = list(map(int, input().split()))
    good[id - 1] += score

total_good = [0] * n
for i in range(1, n) :
    total_good[i] = total_good[parent[i]] + good[i]

print(*total_good)
