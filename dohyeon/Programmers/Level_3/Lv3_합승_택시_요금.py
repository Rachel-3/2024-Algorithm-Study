import heapq

def dijkstra(n, graph, start):
    # 거리 정보를 저장할 리스트, 무한대로 초기화
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        # 이미 처리한 노드면 무시
        if distances[current_node] < current_distance:
            continue
        
        # 인접한 노드 처리
        for adj, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[adj]:
                distances[adj] = distance
                heapq.heappush(queue, (distance, adj))
    
    return distances

def solution(n, s, a, b, fares):
    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
    
    # 각 노드별 최소 거리 정보 저장
    min_costs = []
    for i in range(1, n+1):
        min_costs.append(dijkstra(n, graph, i))
    
    # 모든 합승 지점에 대해 최소 비용 계산
    min_fare = float('inf')
    for i in range(1, n+1):
        total_fare = min_costs[i-1][s] + min_costs[i-1][a] + min_costs[i-1][b]
        if total_fare < min_fare:
            min_fare = total_fare
    
    return min_fare
