bottle = list(map(int, input().split()))

coin = 0
for i in bottle:
    coin += i * 5

print(coin)