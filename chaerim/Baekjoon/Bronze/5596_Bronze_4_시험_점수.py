min = list(map(int, input().split()))
man = list(map(int, input().split()))

sum_min = sum(min)
sum_man = sum(man)

if sum_min >= sum_man:
    print(sum_min)
else:
    print(sum_man)