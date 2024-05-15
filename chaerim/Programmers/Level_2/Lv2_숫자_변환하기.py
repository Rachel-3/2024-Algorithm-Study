def solution(x, y, n):
    answer = 0

    if x == y:
        return answer
    
    value_set = set()
    value = [(x, 0)]
    
    while value:
        current, count = value.pop(0)
        
        if current == y:
            return count

        value_set.add(current)

        for new_current in [current + n, current * 2, current * 3]:
            if new_current == y:
                count += 1
                return count
            elif new_current < y and new_current not in value_set:
                value.append((new_current, count + 1))
                value_set.add(new_current)

    if answer == 0:
        return -1
        
    return answer

'''시간 초과!!
def solution(x, y, n):
    answer = 0

    if x == y:
        return answer
    
    value = [(x, 0)]
    
    while value:
        current, count = value.pop(0)
        
        if current == y:
            answer = count
            break

        for new_current in [current + n, current * 2, current * 3]:
            if new_current <= y:
                value.append((new_current, count + 1))

    if answer == 0:
        return -1
        
    return answer
'''