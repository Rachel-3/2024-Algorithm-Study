# 백준 7795 - 먹을 것인가 먹힐 것인가
# 분류 : 투포인터
# 패캠 해설

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T) :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A = sorted(A)
    B = sorted(B)

    main = 0
    sub = 0
    count = 0

    while main < N :
        if sub == M :
            count += sub
            main += 1
        else :
            if A[main] > B[sub] :
                sub += 1
            else :
                count += sub
                main += 1
    print(count)