def solution(a, b, c, d):
    answer = 0

    dice_num = [a, b, c, d]
    dice_count = {}

    for num in dice_num:
        if num in dice_count:
            dice_count[num] += 1
        else:
            dice_count[num] = 1

    if len(dice_count) == 1:
        return 1111 * a
    
    if 3 in dice_count.values():
        for key in dice_count:
            if dice_count[key] == 3:
                p = key
            else:
                q = key
        return (10 * p + q) ** 2
    
    if sorted(dice_count.values()) == [2, 2]:
        keys = list(dice_count.keys())
        p, q = keys[0], keys[1]
        return (p + q) * abs(p - q)

    
    if 2 in dice_count.values() and len(dice_count) == 3:
        q, r = None, None
        for key in dice_count:
            if dice_count[key] == 1:
                if q is None:
                    q = key
                else:
                    r = key
        return q * r

    if len(dice_count) == 4:
        return min(dice_num)

    return answer