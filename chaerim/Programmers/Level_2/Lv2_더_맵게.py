import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while scoville[0] < K:
        first_min = heapq.heappop(scoville)
        second_min = heapq.heappop(scoville)

        mix_scoville = first_min + (second_min * 2)

        heapq.heappush(scoville,mix_scoville)

        answer += 1

        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer