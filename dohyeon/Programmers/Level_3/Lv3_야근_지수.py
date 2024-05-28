def solution(n, works):
    answer = 0
    if sum(works) < n :
        return 0
    
    # 20점 ㅋ
    # works.sort(reverse = True)
    # index = 0
    # while n > 0 :
    #     if index >= len(works) :
    #         index = index % len(works)
    #     works[index] -= 1
    #     n -= 1
    #     index += 1
    # for i in works :
    #     answer += i ** 2
    
    # 테케 통과, 효율성 꽝
    # works.sort()
    # for i in range(n) :
    #     works[-1] -= 1
    #     works.sort()
    # for i in works :
    #     answer += i ** 2
    
    # 힙사용 - 통과
    import heapq
    works = [-w for w in works]
    heapq.heapify(works)
    for i in range(n) :
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works, i)
    for i in works :
        answer += i ** 2
    
    
    return answer