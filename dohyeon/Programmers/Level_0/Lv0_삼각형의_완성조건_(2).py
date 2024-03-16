def solution(sides):
    answer = 0
    x, y = sides[0], sides[1]
    max_length = max(x, y)
    min_length = min(x, y)
    for i in range(1, max_length + 1) :
        # print(min_length + i)
        if (min_length + i) > max_length :
            answer += 1
    c = max_length
    while max_length + min_length > c :
        answer += 1
        c += 1
    return answer - 1