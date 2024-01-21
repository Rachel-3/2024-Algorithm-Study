d = [[0 for j in range(11)] for i in range(11)]

for i in range(1, 11):
    d[i] = [0] + list(map(int, input().split()))

x=2
y=2

while True:
    if d[x][y] == 0:
        d[x][y] = 9
    elif d[x][y] == 2:
        d[x][y] = 9
        break
    
    if (d[x+1][y] == 1 and d[x][y+1] == 1) or (x==9 and y==9):
        break
    
    if d[x][y+1] != 1:
        y += 1
    elif d[x+1][y] != 1:
        x += 1
    
            
for i in range(1,11):
    for j in range(1,11):
        print(d[i][j], end=' ')
    print()