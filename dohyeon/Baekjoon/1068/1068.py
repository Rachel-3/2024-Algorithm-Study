# 백준 1068 - 트리
# 분류 : 트리

N = int(input())
parenst = list(map(int, input().split()))
R = int(input())

# 루트 노드 찾기
for i in range(N) :
    if parenst[i] == -1 :
        root = i
        break

# 사라지는 노드를 색칠
black = [0] * N
for i in range(N) :
    u = i
    while True :
        if u == R :
            black[i] = 1
            break
        if u == root :
            break

        u = parenst[u]

# 자식이 있는 노드를 색칠
red = [0] * N
for i in range(N) :
    if black[i] == 1 :
        continue

    if i == root :
        continue

    red[parenst[i]] = 1

count = 0
for i in range(N) :
    if black[i] == 1 or red[i] == 1 :
        continue
    count += 1

print(count)