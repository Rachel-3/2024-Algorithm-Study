def solution(n):
    answer = []

    triangle = [[0] * (i + 1) for i in range(n)]

    num = 1
    x, y = -1, 0
    direction = 0
    for i in range(n):
        for _ in range(i, n):
            if direction == 0:
                x += 1
            elif direction == 1:
                y += 1
            elif direction == 2:
                x -= 1
                y -= 1
            triangle[x][y] = num
            num += 1
        direction = (direction + 1) % 3

    answer = sum(triangle, [])

    return answer