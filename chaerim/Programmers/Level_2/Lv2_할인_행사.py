def solution(want, number, discount):
    answer = 0
    
    want_dict = {item: cnt for item, cnt in zip(want, number)}
    
    for day in range(len(discount) - 9):
        discounted_items = {}
        for i in range(day, day + 10):
            if discount[i] in discounted_items:
                discounted_items[discount[i]] += 1
            else:
                discounted_items[discount[i]] = 1
        
        if want_dict == discounted_items:
            answer += 1

    return answer