from collections import deque

n, m, k, x = map(int, input().split())
graphs = [[] for i in range(n + 1)]
for i in range(m) :
    a, b = map(int, input().split())
    graphs[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

queue = deque([x])
while queue :
    now = queue.popleft()
    for next_node in graphs[now] :
        if distance[next_node] == -1 :
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

check = False
for i in range(1, n + 1) :
    if distance[i] == k :
        print(i)
        check = True
if not check :
    print(-1)
