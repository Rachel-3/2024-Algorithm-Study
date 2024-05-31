def solution(topping):
    answer = 0

    left_topping = {}
    right_topping = {}

    for i in topping:
        if i in right_topping:
            right_topping[i] += 1
        else:
            right_topping[i] = 1

    left_count = 0
    right_count = len(right_topping)

    for i in topping:
        if i in left_topping:
            left_topping[i] += 1
        else:
            left_topping[i] = 1
            left_count += 1
        
        right_topping[i] -= 1

        if right_topping[i] == 0:
            right_count -= 1

        if left_count == right_count:
            answer += 1

    return answer