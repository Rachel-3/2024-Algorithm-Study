import math

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

i = math.ceil(a / c)
j = math.ceil(b / d)

max_days = max(i, j)
print(l - max_days)