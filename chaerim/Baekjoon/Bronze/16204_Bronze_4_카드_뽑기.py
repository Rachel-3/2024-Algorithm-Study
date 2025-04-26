n, m, k = map(int, input().split())

answer = min(m, k) + min(n - m, n - k)
print(answer)