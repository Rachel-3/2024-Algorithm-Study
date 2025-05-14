import sys
input = sys.stdin.readline

n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

average = round(sum(numbers) / n)

numbers.sort()
median = numbers[n // 2]

freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0) + 1

max_freq = max(freq.values())
modes = [k for k, v in freq.items() if v == max_freq]
modes.sort()

mode = modes[1] if len(modes) > 1 else modes[0]

value_range = numbers[-1] - numbers[0]

print(average)
print(median)
print(mode)
print(value_range)