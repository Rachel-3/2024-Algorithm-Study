a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a < 0:
    time = (-a) * c
    time += d
    time += b * e
else:
    time = (b - a) * e

print(time)