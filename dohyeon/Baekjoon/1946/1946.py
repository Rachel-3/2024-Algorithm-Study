''' 시간초과 '''
''' -> sys를 통해 입력 받지 않아 시간초과가 일어남
T = int(input())
for i in range(T) :
    N = int(input())
    score = []
    for j in range(N) :
        score.append(list(map(int, input().split())))
    score.sort()
    cnt = 1
    min = score[0][1]
    for j in range(1, N) :
        if score[j][1] < min :
            cnt += 1
            min = score[j][1]
    print(cnt)
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    N = int(input())
    candidates = []
    for _ in range(N) :
        s, m = map(int, input().split())
        candidates.append((s, m))
    
    # (s, m)
    candidates.sort()

    top_ranking = 1e9
    count = 0
    for i in range(N) :
        if candidates[i][1] <top_ranking :
            count += 1
            top_ranking = candidates[i][1]
    
    print(count)

