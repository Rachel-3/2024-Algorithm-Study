l, p = map(int, input().split())
news = list(map(int, input().split()))

peoples = l * p
for i in range(5):
    print(news[i] - peoples, end=' ')