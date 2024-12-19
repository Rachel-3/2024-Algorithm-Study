# 백준 2309 - 일곱 난쟁이
# 분류 : 브루트포스 알고리즘
# 패캠 해설

from itertools import combinations

heights = []
for _ in range(9)  :
    height = int(input())
    heights.append(height)

for a in combinations(heights, 7) :
    if sum(a) == 100 :
        a = list(a)
        a.sort()
        for x in a :
            print(x)
        break
        
    