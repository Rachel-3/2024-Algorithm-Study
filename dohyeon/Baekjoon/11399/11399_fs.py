# 백준 11399 - ATM
# 분류 : 그리디
# 패캠 해설

N = int(input())
P = list(map(int, input().split()))

P = sorted(P)

waiting = [0] * N
waiting[0] = P[0]
for i in range(1, N) :
    waiting[i] = waiting[i - 1] + P[i]

print(sum(waiting))