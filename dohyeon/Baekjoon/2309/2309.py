# 백준 2309 - 일곱 난쟁이
# 분류 : 브루트포스 알고리즘
from itertools import combinations
peoples = []
for i in range(9) :
    peoples.append(int(input()))

result = []
for i in combinations(peoples, 7) :
    if sum(i) == 100 :
        result = list(i)
        break

result.sort()
for i in result :
    print(i)