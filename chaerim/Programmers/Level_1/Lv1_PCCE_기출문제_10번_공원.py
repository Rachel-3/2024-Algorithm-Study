def solution(mats, park):
    answer = 0

    n, m = len(park), len(park[0])
    dp = [[0] * m for _ in range(n)]

    max_mat_size = 0
    for i in range(n):
        for j in range(m):
            if park[i][j] == '-1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                max_mat_size = max(max_mat_size, dp[i][j])

    mats.sort(reverse = True)
    for mat in mats:
        if mat <= max_mat_size:
            return mat

    return -1