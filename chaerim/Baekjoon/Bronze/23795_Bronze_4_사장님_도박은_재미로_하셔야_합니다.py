total = 0

while True:
    money = int(input())
    if money == -1:
        break
    total += money

print(total)