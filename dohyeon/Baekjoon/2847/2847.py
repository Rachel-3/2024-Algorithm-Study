# 백준 2847 - 게임을 만든 동준이
# 분류 : 그리디

N = int(input())
levels = []
for i in range(N) :
    levels.append(int(input()))

count = 0
for i in range(N - 2, -1, -1) :
    if levels[i] >= levels[i + 1] :
        count += levels[i] - (levels[i + 1] - 1)
        levels[i] = levels[i + 1] - 1
print(count)