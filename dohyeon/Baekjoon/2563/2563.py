# 백준 2563 - 색종이
# 분류 : 구현

N = int(input())
result = 0
array = [[0] * 100 for _ in range(100)]

for _ in range(N) :
    y, x = map(int, input().split())
    for i in range(x, x + 10) :
        for j in range(y, y + 10) :
            array[i][j] = 1

for i in range(100) :
    result += array[i].count(1)
print(result)
    
