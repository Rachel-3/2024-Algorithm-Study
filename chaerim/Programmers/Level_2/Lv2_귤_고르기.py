def solution(k, tangerine):
    answer = 0

    count_dict = {}
    for size in tangerine:
        if size in count_dict:
            count_dict[size] += 1
        else:
            count_dict[size] = 1

    sorted_counts = sorted(count_dict.values(), reverse=True)

    for count in sorted_counts:
        if k > 0:
            k -= count
            answer += 1
        else:
            break

    return answer