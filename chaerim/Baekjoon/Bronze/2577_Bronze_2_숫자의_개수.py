mul = 1
for _ in range(3):
    a = int(input())
    mul *= a

counts = [0] * 10

for i in str(mul):
    counts[int(i)] += 1

for count in counts:
    print(count)