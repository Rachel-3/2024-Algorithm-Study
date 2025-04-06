a, b, c = map(int, input().split())
d = int(input())

total_time = a * 3600 + b * 60 + c

total_time += d

total_time %= 24 * 3600

h = total_time // 3600
m = (total_time % 3600) // 60
s = total_time % 60

print(h, m ,s)