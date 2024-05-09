def solution(num_list):
    answer = 0

    even_number = 0
    odd_number = 0
    for num in range(len(num_list)):
        if num%2 == 0:
            even_number += num_list[num]
        else:
            odd_number += num_list[num]

    if even_number >= odd_number:
        answer = even_number
    else:
        answer = odd_number

    return answer