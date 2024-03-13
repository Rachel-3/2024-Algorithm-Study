def solution(n):
    answer = 0

    for num in range(1, n+1):
        list = []
        for i in range(1, num+1):
            if num%i == 0:
                list.append(i)
            
            if len(list) >= 3:
                answer += 1
                break

    return answer