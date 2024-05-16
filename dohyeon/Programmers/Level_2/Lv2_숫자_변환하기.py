''' 순수 BFS 사용 '''
def solution(x, y, n) :
    answer = 0
    visited = set()
    visited.add(x)
    while visited :
        if y in visited :
            return answer
        not_visited = set()
        
        for i in visited :
            if i + n <= y :
                not_visited.add(i + n)
            if i * 2 <= y :
                not_visited.add(i * 2)
            if i * 3 <= y :
                not_visited.add(i * 3)
        visited = not_visited
        answer += 1
    return -1

''' deque 사용 & BFS '''
from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append([x, 0])
    visited = set()
    while queue :
        i, j = queue.popleft()
        if i > y or i in visited :
            continue
        visited.add(i)
        if i == y :
            return j
        for k in (i * 3, i * 2, i + n) :
            if k <= y and k not in visited :
                queue.append([k, j + 1])
    return -1