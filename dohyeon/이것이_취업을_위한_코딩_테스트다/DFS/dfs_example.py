def dfs(graph, v, visitied) :
    visitied[v] = True
    print(v, end = ' ')

    for i in graph[v] :
        if not visitied[i] :
            dfs(graph, i, visitied)
    

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)