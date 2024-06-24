def solution(array):
    answer = 0

    array.sort()
    array_len = len(array)
    answer = array[array_len//2]

    return answer