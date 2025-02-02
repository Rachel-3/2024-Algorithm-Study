# 백준 11725 - 트리의 부모 찾기
# 분류 : DFS

import sys
sys.setrecursionlimit(10**6)
# input = sys.stdin.readline()

N = int(input())

adj = [[] for _ in range(N)] # 인접리스트
for i in range(N - 1) :
    a, b = list(map(int, input().split()))
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

visit = [False] * (N + 1)
parent = [-1] * (N + 1)

# DFS
def dfs(u) :
    visit[u] = True
    for v in adj[u] :
        if not visit[v] :
            parent[v] = u
            dfs(v)
dfs(0)

for i in range(1, N) :
    print(parent[i] + 1)
