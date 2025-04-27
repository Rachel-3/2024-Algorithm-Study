n, w, h, l = map(int, input().split())

cols = w // l
rows = h // l

max_cows = cols * rows

print(min(max_cows, n))