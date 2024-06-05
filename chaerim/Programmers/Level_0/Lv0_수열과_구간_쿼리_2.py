def solution(arr, queries):
    answer = []

    for query in queries:
        start, end, num = query
        new_arr = arr[start:end+1]
        small_num = -1
        for i in new_arr:
            if i > num and (small_num == -1 or i < small_num):
                small_num = i

        answer.append(small_num)

    return answer

print(solution([0, 1, 2, 4, 3], [[0, 4, 2],[0, 3, 2],[0, 2, 2]]))