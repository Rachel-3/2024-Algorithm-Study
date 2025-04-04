k, n, m = map(int, input().split())

a = (k * n) - m
if a <= 0:
    print(0)
else:
    print(a)