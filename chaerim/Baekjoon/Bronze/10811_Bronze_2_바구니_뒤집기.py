n, m = map(int, input().split())

bucket = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    bucket = bucket[:i-1] + bucket[i-1:j][::-1] + bucket[j:]

print(*bucket)