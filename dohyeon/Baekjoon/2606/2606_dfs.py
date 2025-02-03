# 백준 2606 - 바이러스
# 분류 : DFS

N = int(input())
M = int(input())

adj = [[] for i in range(N)]

for _ in range(M) :
    a, b = list(map(int, input().split()))
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

visit = [False] * N

# dfs
def dfs(u) :
    visit[u] = True

    for v in adj[u] :
        if not visit[v] :
            dfs(v)

dfs(0)

count = 0

for i in range(1, N) :
    if visit[i] :
        count += 1

print(count)