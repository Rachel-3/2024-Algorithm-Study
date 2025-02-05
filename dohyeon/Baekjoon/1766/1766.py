# 백준 1766 - 문제집
# 분류 : 위상 정렬

'''
조건 1. 왠만하면 쉬운거 부터 풀래
조건 2. 먼저 풀면 좋은 문제가 주어짐

예를 들어
3번 -> 1번이 있으면 3번 문제를 풀면 1번 문제를 풀때 도움이 됨!
4번 -> 2번이 있으면 4번 문제를 풀면 2번 문제를 풀떄 도움이 됨!

문제 풀이 조건
1. N개의 문제를 모두 풀어야함
2. 먼저 푸는게 좋은 문제가 있으면 먼저 푼다.
3. 가능하면 쉬운 문제부터 푼다.
'''

from queue import PriorityQueue

N, M = list(map(int, input().split()))

adj = [[] for _ in range(N)]
need_to_learn = [0] * N

for _ in range(M) :
    a, b = list(map(int, input().split()))

    adj[a - 1].append(b - 1)
    need_to_learn[b - 1] += 1

# 위상정렬
pq = PriorityQueue()

for i in range(N) :
    if need_to_learn[i] == 0 :
        pq.put(i)

learn = []
while pq.qsize() != 0 :
    u = pq.get(i)

    learn.append(u)

    for v in adj[u] :
        need_to_learn[v] -= 1
        if need_to_learn[v] == 0 :
            pq.put(v)

for i in range(N) :
    print(learn[i] + 1, end = " ")