from collections import deque

def solution(maps):
    answer = 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, +1, 0]
    x = len(maps)
    y = len(maps[0])
    answer = maze_bfs(maps, x, y, dx, dy, (0,0))
    return answer

def valid_pt(maps, x, y, point) :
    if point[0] < 0 or point[0] >= x or point[1] < 0 or point[1] >= y :
        return False
    elif maps[point[0]][point[1]]==1:
        return True
    else :
        return False

def maze_bfs(maps, x, y, dx, dy, start) :
    q = deque()
    q.append(start)
    while q :
        cur_pt = q.popleft()
        for i in range(4) :
            next_pt = cur_pt[0] + dx[i], cur_pt[1] + dy[i]
            if valid_pt(maps, x, y, next_pt):
                maps[next_pt[0]][next_pt[1]]+=maps[cur_pt[0]][cur_pt[1]]
                q.append(next_pt)
    if (maps[x-1][y-1]) == 1 :
        return (-1)
    else :
        return (maps[x-1][y-1])
