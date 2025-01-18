a = int(input())

paper = [[0] * 100 for _ in range(100)]

for _ in range(a):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[j][i] = 1

result = 0
for row in paper:
    result += sum(row)

print(result)