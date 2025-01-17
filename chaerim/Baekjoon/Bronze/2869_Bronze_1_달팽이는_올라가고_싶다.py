a, b, v = map(int, input().split())

days = (v - b + (a - b - 1)) // (a - b)
print(days)