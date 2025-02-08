# 백준 22864 - 피로도
# 분류 : 그리디

A, B, C, M = list(map(int, input().split()))

piro = 0
work = 0

for i in range(24) :
    if piro + A > M :
        piro -= C
        piro = max(0, piro)
    else :
        piro += A
        work += B

print(work)