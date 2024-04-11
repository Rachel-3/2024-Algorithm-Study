from collections import deque
def solution(cacheSize, cities):
    LRU = deque(maxlen = cacheSize)
    cities = [n.lower() for n in cities]
    answer = 0
    for city in cities :
        if city not in LRU :
            LRU.append(city)
            answer += 5
        else :
            LRU.remove(city)
            LRU.append(city)
            answer += 1
    return answer

# def solution(cacheSize, cities):
#     answer = 0
#     LRU = []
#     cities = [n.lower() for n in cities]
#     for i in cities :
#         if i in LRU :
#             LRU.remove(i)
#             LRU.append(i)
#             answer += 1
#         else :
#             if len(LRU) > cacheSize :
#                 LRU.pop(0)
#             LRU.append(i)
#             answer += 5
#     return answer

# def solution(cacheSize, cities):
#     answer = 0
#     LRU = []
#     cities = [n.lower() for n in cities]
#     if cacheSize == 0 :
#         return len(cities) * 5
#     for i in cities :
#         if not i in LRU :
#             if len(LRU) <= cacheSize :
#                 LRU.append(i)
#             else :
#                 LRU.pop(0)
#                 LRU.append(i)
#             answer += 5
#         else :
#             LRU.pop(LRU.index(i))
#             LRU.append(i)
#             answer += 1
#     return answer