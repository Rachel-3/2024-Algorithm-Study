def solution(s):
    data = {}
    for i in s :
        if i in data :
            data[i] += 1
        else :
            data[i] = 1
    result = [key for key, value in data.items() if value == 1]
    result.sort()
    return "".join(result)