numbers = list(range(1, 31))
for _ in range(28):
    n = int(input())
    numbers.remove(n)

print(min(numbers))
print(max(numbers))