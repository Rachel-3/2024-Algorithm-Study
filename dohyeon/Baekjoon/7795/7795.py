# 백준 7795 - 먹을 것인가 먹힐 것인가
# 분류 : 투포인터

# 결과 - 시간 초과

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T) :
    N, M = map(int, input().split())
    count = 0
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in A :
        for j in B :
            if i > j :
                count += 1
    print(count)