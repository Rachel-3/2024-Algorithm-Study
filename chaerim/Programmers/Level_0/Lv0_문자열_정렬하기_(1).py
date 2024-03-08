def solution(my_string):
    answer = []

    for i in my_string:
        if i.isdigit():
            num = int(i)
            if num >= 0:
                answer.append(num)

    answer.sort()

    return answer