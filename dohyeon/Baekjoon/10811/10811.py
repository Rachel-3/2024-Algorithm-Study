# 백준 10811 - 바구니 뒤집기

N, M = map(int, input().split())
basket = [i for i in range(1, N + 1)]

for _ in range(M) :
    i, j = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1]

print(*basket)
