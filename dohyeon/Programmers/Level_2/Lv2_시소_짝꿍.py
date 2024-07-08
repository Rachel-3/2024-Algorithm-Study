'''
어느 공원 놀이터에는 시소가 하나 설치되어 있습니다. 이 시소는 중심으로부터 2(m), 3(m), 4(m) 거리의 지점에 좌석이 하나씩 있습니다.
이 시소를 두 명이 마주 보고 탄다고 할 때, 시소가 평형인 상태에서 각각에 의해 시소에 걸리는 토크의 크기가 서로 상쇄되어 완전한 균형을 이룰 수 있다면 그 두 사람을 시소 짝꿍이라고 합니다.
즉, 탑승한 사람의 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같다면 시소 짝꿍이라고 할 수 있습니다.
사람들의 몸무게 목록 weights이 주어질 때, 시소 짝꿍이 몇 쌍 존재하는지 구하여 return 하도록 solution 함수를 완성해주세요.
'''
'''
{100, 100} 은 서로 같은 거리에 마주보고 앉으면 균형을 이룹니다.
{180, 360} 은 각각 4(m), 2(m) 거리에 마주보고 앉으면 균형을 이룹니다.
{180, 270} 은 각각 3(m), 2(m) 거리에 마주보고 앉으면 균형을 이룹니다.
{270, 360} 은 각각 4(m), 3(m) 거리에 마주보고 앉으면 균형을 이룹니다.
'''

''' 시간 초과 및 실패 23.5/100 '''
'''
from itertools import combinations

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solution(weights):
    answer = 0
    sisos = list(combinations(weights, 2))
    gcd_sheets = [1, 2, 3, 4]
    for i in sisos :
        if i[0] == i[1] :
            answer += 1
        elif i[0] // gcd(i[0], i[1]) in gcd_sheets and i[1] // gcd(i[0], i[1]) in gcd_sheets :
            answer += 1

    return answer

print(solution([100,180,360,100,270])) #4
'''
''' 실패 47.1 / 100'''
# from itertools import combinations
# from math import gcd

# def solution(weights):
#     answer = 0
#     weight_count = {}
#     for weight in weights:
#         if weight in weight_count:
#             weight_count[weight] += 1
#         else:
#             weight_count[weight] = 1
    
#     for count in weight_count.values():
#         if count > 1:
#             answer += count * (count - 1) // 2
#     gcd_sheets = {1, 2, 3, 4}
#     for (w1, w2) in combinations(weight_count.keys(), 2):
#         g = gcd(w1, w2)
#         if (w1 // g in gcd_sheets) and (w2 // g in gcd_sheets):
#             answer += weight_count[w1] * weight_count[w2]

#     return answer

# print(solution([100, 180, 360, 100, 270])) # 4

# from collections import Counter
# def solution(weights) :
#     answer = 0
#     weight_count = Counter(weights)
#     ratios = [(2, 2), (2, 3), (2, 4), (3, 4)]
#     for weights, count in weight_count.items() :
#         if count > 1 :
#             answer += count * (count - 1) // 2
#     diffrent_weights = list(weight_count.keys())
#     for i in range(len(diffrent_weights)) :
#         for j in range(i + 1, len(diffrent_weights)) :
#             w1, w2 = diffrent_weights[i], diffrent_weights[j]
#             for ratio in ratios :
#                 if w1 * ratio[1] == w2 * ratio[0] : 
#                     answer += weight_count[w1] * weight_count[w2]
#                     break
#     return answer

# print(solution([100, 180, 360, 100, 270])) # 4


# from itertools import combinations
# from math import gcd
# def solution(weights):
#     answer = 0
#     weight_count = {}
#     for weight in weights:
#         if weight in weight_count:
#             weight_count[weight] += 1
#         else:
#             weight_count[weight] = 1
    
#     for count in weight_count.values():
#         if count > 1:
#             answer += int(count * (count - 1) // 2)
#     gcd_sheets = {1, 2, 3, 4}
#     for (w1, w2) in combinations(weight_count.keys(), 2):
#         g = gcd(w1, w2)
#         if (int(w1 // g) in gcd_sheets) and (int(w2 // g) in gcd_sheets):
#             answer += int(weight_count[w1] * weight_count[w2])

#     return answer


from collections import Counter

def solution(weights) :
    answer = 0
    count = Counter(weights)
    for k, v in count.items() :
        if v > 1 :
            answer += v * (v - 1) / 2
    weights = list(set(weights))
    check = (3/ 4, 2 / 3, 1 / 2)
    for w in weights :
        for c in check :
            if w * c in weights :
                answer += count[w] * count[w * c]
    return int(answer)

print(solution([100, 180, 360, 100, 270])) # 4
