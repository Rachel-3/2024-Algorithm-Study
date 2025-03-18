a = input().upper()
counts = {}

for i in a:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

max_count = max(counts.values())

common = [k for k, v in counts.items() if v == max_count]

if len(common) > 1:
    print("?")
else:
    print(common[0])