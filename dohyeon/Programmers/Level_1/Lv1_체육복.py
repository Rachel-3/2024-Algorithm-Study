def solution(n, lost, reserve) :
    t1 = set(lost)
    t2 = set(reserve)
    lost = list(t1 - t2)
    reserve = list(t2 - t1)
    answer = n - len(lost)
    for i in range(len(reserve)) :
        for j in lost :
            if j == reserve[i] - 1 or j == reserve[i] + 1 :
                answer += 1
                lost.remove(j)
                break
            elif j == reserve[i] :
                answer += 1
                lost.remove(j)
                break

    return answer

print(solution(5, [2, 4], [1, 3, 5])) # 5
print(solution(5, [2, 4], [3])) # 4
print(solution(3, [3], [1])) # 2
print(solution(3, [1, 2, 3], [1, 2, 3])) # 3
print(solution(7, [1, 3, 5, 7], [1, 3, 5, 7])) # 7
print(solution(5, [4, 5], [3, 4])) # 4