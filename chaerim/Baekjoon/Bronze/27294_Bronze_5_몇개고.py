t, s = map(int, input().split())

is_lunch = (12 <= t <= 16)

if is_lunch and s == 0:
    print(320)
else:
    print(280)