n, m = map(int, input().split())

yy = [i+1 for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    yy[i - 1], yy[j - 1] = yy[j - 1], yy[i - 1]

print(' '.join(map(str, yy)))