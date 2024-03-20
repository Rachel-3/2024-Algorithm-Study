def solution(numbers):
    answer = 0
    numbers.sort()

    max1, max2 = numbers[-1], numbers[-2]

    answer = max1 * max2

    return answer