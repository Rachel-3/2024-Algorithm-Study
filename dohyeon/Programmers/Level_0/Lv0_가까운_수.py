def solution(array, n):
    answer = 0
    array.sort()
    stack = []
    for i in array :
        stack.append(abs(n - i))
    answer = array[stack.index(min(stack))]
    return answer