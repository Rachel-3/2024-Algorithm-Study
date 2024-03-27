def solution(numlist, n):
    answer = []

    difference_dict = {}
    for num in numlist:
        difference_dict[num] = abs(num - n)

    sorted_difference_dict = sorted(difference_dict.items(), key=lambda x: (x[1], -x[0]))

    answer = [i for i, _ in sorted_difference_dict]

    return answer