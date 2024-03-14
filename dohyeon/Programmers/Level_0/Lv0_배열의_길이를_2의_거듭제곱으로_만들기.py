def solution(arr):
    count = 0
    while len(arr) != 2 ** count:
        if len(arr) == 2 ** count:
            break
        if len(arr) > 2 ** count:
            count += 1
        else:
            result = (2 ** count) - len(arr)
            for i in range(result):
                arr.append(0)
    return arr