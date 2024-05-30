def solution(m, n, puddles):
    answer = 0
    maps = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i, j in puddles :
        maps[j][i] = 1
    
    maps[0][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if maps[i][j] :
                maps[i][j] = 0
            else:
                maps[i][j] = (maps[i - 1][j] + maps[i][j - 1]) % 1000000007
    return maps[-1][-1]

print(solution(4, 3, [[2, 2]]))