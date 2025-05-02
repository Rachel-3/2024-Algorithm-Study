A, B, C = map(int, input().split())

results = [
    (A * B) / C,
    (A / B) * C,
    A * (B / C),
    A / (B * C)
]

print(int(max(results)))