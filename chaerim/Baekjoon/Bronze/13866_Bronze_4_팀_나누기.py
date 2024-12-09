o = list(map(int, input().split()))

o.sort()
print(abs((o[0] + o[3]) - (o[1] + o[2])))