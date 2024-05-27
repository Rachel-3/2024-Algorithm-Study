import heapq
def solution(operations):
    answer = []
    heap = []
    heapq.heapify(heap)
    for i in operations :
        method, value = i.split(" ")[0], int(i.split(" ")[1])
        if method == "I" :
            heapq.heappush(heap, value)
            
        else :
            if len(heap) == 0 :
                pass
            elif method == "D" and value == -1 :
            # 최소값 삭제
                heapq.heappop(heap)
            elif method == "D" and value == 1 :
                heap.remove(max(heap))
                heapq.heapify(heap)
    if len(heap) == 0 :
        return [0, 0]
    else :
        answer = [max(heap), min(heap)]
    return answer