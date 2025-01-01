# 백준 10819 - 차이를 최대로 - 패캠 해설
from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

max_diff_sum = 0
for a in permutations(A, N) :
    diff_sum = 0
    for i in range(N - 1) :
        diff_sum += abs(a[i] - a[i + 1])
    max_diff_sum = max(max_diff_sum, diff_sum)

print(max_diff_sum)