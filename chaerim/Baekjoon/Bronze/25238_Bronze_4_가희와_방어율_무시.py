a, b = map(int, input().split())

if a * (100 - b) < 10000:
    print(1)
else:
    print(0)