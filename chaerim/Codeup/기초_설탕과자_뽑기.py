h, w = map(int, input().split())
p = [[0 for w in range(w)] for h in range(h)]

n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            p[x - 1][y + j - 1] = 1

        if d == 1:
            p[x + j - 1][y - 1] = 1

for i in range(h):
    for j in range(w):
        print(p[i][j], end = ' ')
    print()