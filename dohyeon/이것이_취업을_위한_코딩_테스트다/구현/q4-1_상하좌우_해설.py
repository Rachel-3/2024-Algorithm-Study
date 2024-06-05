N = int(input())
routes = list(map(str,  input().split(" ")))

x,  y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for route in routes :
    for i in range(len(move_types)) :
        if route == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > N or ny < 1 or ny > N :
        continue
    x, y = nx, ny
print(x, y)
