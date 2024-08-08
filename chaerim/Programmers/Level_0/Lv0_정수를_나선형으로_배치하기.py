def solution(n):
    answer = [[0] * n for _ in range(n)]

    num = 1
    direction = 0
    x, y = 0, 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for _ in range(n * n):
        answer[x][y] = num
        num += 1

        next_x, next_y = x + directions[direction][0], y + directions[direction][1]

        if not (0 <= next_x < n and 0 <= next_y < n and answer[next_x][next_y] == 0):
            direction = (direction + 1) % 4
            next_x, next_y = x + directions[direction][0], y + directions[direction][1]

        x, y = next_x, next_y

    return answer