a, b = map(int, input().split())
c = int(input())

account_total = a + b
chicken_price = c * 2
if account_total >= chicken_price:
    print(account_total - chicken_price)
else:
    print(account_total)