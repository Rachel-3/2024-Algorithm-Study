s = input().strip()
max_sum = -1

for i in range(1, min(3, len(s))):
    a = int(s[:i])
    b = int(s[i:])
    if 1 <= a <= 10 and 1 <= b <= 10:
        max_sum = max(max_sum, a + b)

print(max_sum)