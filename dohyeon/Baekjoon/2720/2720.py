# 백준 2720 - 세탁소 사장 동혁
# 분류 : 수학

moneys = [25, 10, 5, 1]
T = int(input())
for i in range(T) :
    C = int(input())
    for coin in moneys :
        print("%d" % (C // coin), end = " ")
        C %= coin
    print()