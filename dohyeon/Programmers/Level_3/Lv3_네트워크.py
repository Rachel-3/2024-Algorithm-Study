def solution(n, computers):
    def dfs(vector) :
        visited[vector] = True
        for i in range(n) :
            if visited[i] == False and computers[vector][i] == True :
                dfs(i)
    answer = 0
    visited = [False] * n
    for i in range(n) :
        if visited[i] == False :
            dfs(i)
            answer += 1

    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))