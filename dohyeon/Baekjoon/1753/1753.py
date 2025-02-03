# 백준 1753 - 최단 경로
# 분류 : 최단거리

import sys
from queue import PriorityQueue

input = sys.stdin.readline

V, E = list(map(int, input().split()))
K = int(input()) - 1

adj = [[] for _ in range(V)]
for _ in range(E) :
    u, v, w = list(map(int, input().split()))
    adj[u - 1].append((v - 1, w))

# 다익스트라 알고리즘
dist = [1e9] * V
pq = PriorityQueue()

dist[K] = 0
pq.put((0, K))

while pq.qsize() != 0 :
    d, u = pq.get()
    
    if d != dist[u] :
        continue
    
    for v, w in adj[u] :
        if dist[v] > dist[u] + w :
            dist[v] = dist[u] + w
            pq.put((dist[v], v))

for i in range(V) :
    if dist[i] == 1e9 :
        print("INF")
    else :
        print(dist[i])