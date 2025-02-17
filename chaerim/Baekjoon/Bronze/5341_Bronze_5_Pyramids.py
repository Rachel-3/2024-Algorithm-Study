while True:
    n = int(input())
    if n == 0:
        break
    else:
        total = 0
        for i in range(n, 0, -1):
            total += i
        print(total)