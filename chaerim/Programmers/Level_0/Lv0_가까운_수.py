def solution(array, n):
    answer = 0
    difference = None

    for i in array:
        current_difference = abs(n - i)

        if difference is None:
            difference = current_difference
            answer = i
        elif current_difference < difference:
            difference = current_difference
            answer = i
        elif current_difference == difference and answer > i:
            answer = i

    return answer