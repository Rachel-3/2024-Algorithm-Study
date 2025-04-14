science = [int(input()) for _ in range(4)]
social = [int(input()) for _ in range(2)]

total = sum(sorted(science, reverse=True)[:3]) + max(social)
print(total)