# 백준 2444 - 별 찍기 - 7
# 분류 : 구현

N = int(input())
count = 1
for i in range(1, N + 1) :
    for j in range(N - i) :
        print(" ", end = "")
    for j in range(2 * i - 1) :
        print("*", end = "")
    print()
for i in range(N - 1, 0, -1) :
    for j in range(N - i) :
        print(" ", end = "")
    for j in range(2 * i - 1) :
        print("*", end = "")
    print()
