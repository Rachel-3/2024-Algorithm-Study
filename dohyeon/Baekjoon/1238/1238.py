# 백준 1238 - 파티
# 분류 : 최단거리

import sys
from queue import PriorityQueue

input = sys.stdin.readline

N, M, X = list(map(int, input().split()))
X -= 1

adj = [[] for _ in range(M)]
reverse_ajd = [[] for _ in range(M)]

for i in range(M) :
    u, v, w = list(map(int, input().split()))
    
    # 방향이 있고, 가중치가 있기 때문에 튜플로 넣기
    adj[u - 1].append((v - 1, w))
    reverse_ajd[v - 1].append((u - 1, w))

# 원래 그래프에서 다익스트라
dist = [1e9] * N
pq = PriorityQueue()

dist[X] = 0
pq.put((0, X))

while pq.qsize() != 0 :
    d, u = pq.get()
    
    if d != dist[u] :
        continue

    for v, w in adj[u] :
        if dist[v] > dist[u] + w :
            dist[v] = dist[u] + w
            pq.put((dist[v], v))

# 역그래프에서 다익스트라
reverse_dist = [1e9] * N
pq = PriorityQueue()

reverse_dist[X] = 0
pq.put((0, X))

while pq.qsize() != 0 :
    d, u = pq.get()

    if d != reverse_dist[u] :
        continue

    for v, w in reverse_ajd[u] :
        if reverse_dist[v] > reverse_dist[u] + w :
            reverse_dist[v] = reverse_dist[u] + w
            pq.put((reverse_dist[v], v))

max_dist = 0
for i in range(N) :
    if max_dist < dist[i] + reverse_dist[i] :
        max_dist = dist[i] + reverse_dist[i]

print(max_dist)
