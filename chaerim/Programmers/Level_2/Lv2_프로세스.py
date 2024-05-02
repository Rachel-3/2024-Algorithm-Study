def solution(priorities, location):
    answer = 0

    while priorities:
        num = priorities.pop(0)
        for p in priorities:
            if p > num:
                priorities.append(num)
                break
        else:
            answer += 1
            if location == 0:
                return answer
        location -= 1
        if location < 0:
            location = len(priorities) - 1
    return answer