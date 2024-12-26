# 백준 10819 - 차이를 최대로
from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

max_sum = 0
for perm in permutations(A) :
    sum = 0
    for i in range(N - 1) :
        sum += abs(perm[i] - perm[i + 1])
    max_sum = max(max_sum, sum)

print(max_sum)