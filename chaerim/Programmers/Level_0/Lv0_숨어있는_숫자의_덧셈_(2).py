def solution(my_string):
    answer = 0

    num_box = ""
    for i in my_string:
        if i.isdigit():
            num_box += i
        else:
            if num_box:
                answer += int(num_box)
                num_box = ""

    if num_box:
        answer += int(num_box)

    return answer