s = int(input())

for i in range(1, s + 1):
    print(' ' * (s - i) + '*' * (2 * i - 1))

for i in range(s - 1, 0, -1):
    print(' ' * (s - i) + '*' * (2 * i - 1))