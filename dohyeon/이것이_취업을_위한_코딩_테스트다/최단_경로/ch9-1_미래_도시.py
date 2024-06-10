INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용은 0
for a in range(1, n + 1) :
    for b in range(1, n + 1) :
        if a == b :
            graph[a][b] = 0

for i in range(m) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n + 1) :
    for a in range(1, n + 1) :
        for b in range(1, n + 1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
distance = graph[1][k] + graph[k][x]

if distance >= INF :
    print("INFINITY")
else :
    print(distance)

''' ex 1
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

3
'''
''' ex 2
4 2
1 3
2 4
3 4

-1
'''