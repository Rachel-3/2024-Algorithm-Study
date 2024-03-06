def solution(array, height):
    answer = 0

    array = sorted(array, reverse=True)

    for arr in array[-1::-1]:
        if arr <= height:
            array.pop()
    
    answer = len(array)

    return answer