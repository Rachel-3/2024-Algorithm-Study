# 백준 2559 - 수열
# 분류 : 누적합

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
temperature = list(map(int, input().split()))

sums = [0] * (N + 1)
for i in range(1, N + 1):
    sums[i] = sums[i - 1] + temperature[i - 1]

max_sum = -100000
for i in range(N - K + 1):
    max_sum = max(max_sum, sums[i + K] - sums[i])

print(max_sum)