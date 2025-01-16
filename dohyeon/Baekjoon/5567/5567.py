# 백준 5567 - 결혼식
# 분류 : 그래프

n = int(input())
m = int(input())

adj = [[] for _ in range(n)]

for _ in range(m) :
    a, b = list(map(int, input().split()))
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

friend = [0] * n

for i in adj[0] :
    friend[i] = 1

friend_of_friend = [0] * n
for i in range(n) :
    if friend[i] == 0 :
        continue
    
    for j in adj[i] :
        if j != 0 and friend[j] == 0 :
            friend_of_friend[j] = 1

print(sum(friend) + sum(friend_of_friend))