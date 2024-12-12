# 백준 2847 - 게임을 만든 동준이
# 분류 : 그리디
# 패캠 해설

N = int(input())
L = []
for i in range(N) :
    L.append(int(input()))

count = 0
for i in range(N - 2, -1, -1) :
    if L[i] >= L[i + 1] :
        count += L[i] - (L[i + 1] - 1)
        L[i] = L[i + 1] - 1
print(count)