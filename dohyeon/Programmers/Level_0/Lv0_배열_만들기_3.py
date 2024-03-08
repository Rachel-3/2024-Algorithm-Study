def solution(arr, intervals):
    answer = []
    for i in intervals :
        for idx, value in enumerate(arr) :
            if idx >= i[0] and idx <= i[1] :
                answer.append(value)
    return answer

print(solution([1, 2, 3, 4, 5], [[1, 3], [0, 4]]))