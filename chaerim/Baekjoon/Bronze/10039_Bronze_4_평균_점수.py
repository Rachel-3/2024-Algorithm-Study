scores = [int(input()) for _ in range(5)]

sum_score = 0
for i in scores:
    if i < 40:
        sum_score += 40
    else:
        sum_score += i

print(sum_score//5)