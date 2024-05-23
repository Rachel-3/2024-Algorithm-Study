N = int(input())
scared = list(map(int, input().split()))
answer = 0
scared.sort()

count = 0
for i in scared :
    count += 1
    if count >= i :
        answer += 1
        count = 0

print(answer)
