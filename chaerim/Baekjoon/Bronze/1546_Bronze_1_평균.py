n = int(input())

scores = list(map(int, input().split()))

m = max(scores)
new_scores = []
for i in range(n):
    new_scores.append(scores[i]/m * 100)

print(sum(new_scores) / len(new_scores))