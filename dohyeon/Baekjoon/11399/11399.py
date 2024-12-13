# 백준 11399 - ATM
# 분류 : 그리디

N = int(input())
P = list(map(int, input().split()))

P = sorted(P)

result = [0] * N
result[0] = P[0]
for i in range(1, N) :
    result[i] = result[i - 1] + P[i]

print(sum(result))