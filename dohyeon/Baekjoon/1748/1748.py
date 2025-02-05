# 백준 1748 - 수 이어 쓰기 1

''' 시간 초과 '''
'''
N = int(input())

answer = ""

current = 1
for i in range(N) :
    answer += str(current)
    current += 1

print(len(answer))
'''

left = [
    1, 
    10,
    100, 
    1000,
    10000,
    100000,
    1000000,
    10000000,
    100000000
]

right = [
    9,
    99,
    999,
    9999,
    99999,
    999999,
    9999999,
    99999999,
    999999999   
]

N = int(input())

sum = 0
for i in range(len(left)) :
    if N >= left[i] and N <= right[i] :
        sum += (N - left[i] + 1) * (i + 1)
        break
    else :
        sum += (right[i] - left[i] + 1) * (i + 1)

print(sum)