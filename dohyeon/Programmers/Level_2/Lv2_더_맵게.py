''' 80 점 소스'''
'''
def solution(scoville, K):
    answer = 0
    temp = []
    i = 0
    result = False
    while True :
        for value in scoville :
            if value >= K :
                result = True
            else :
                result = False
                break
        if result == False :    
            if scoville[i] < K :
                scoville[i] = scoville[i] + (scoville[i + 1] * 2)
                del scoville[i + 1]
                scoville.sort()
                answer += 1
        else :
            break
    return answer
'''

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while len(scoville) > 1 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        answer += 1
    if scoville[0] < K:
        return -1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
