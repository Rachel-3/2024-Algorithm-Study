# 백준 10831 - 공 바꾸기
N, M = map(int, input().split())
baksets = [i for i in range(1, N + 1)]
temp = 0

for i in range(M) :
    A, B = map(int, input().split())
    baksets[A - 1], baksets[B - 1] = baksets[B - 1], baksets[A - 1]

for i in range(N) :
    print(baksets[i], end = " ")