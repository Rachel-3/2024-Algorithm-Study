def solution(x):
    answer = True

    x_sum = 0
    for i in str(x):
        x_sum += int(i)
    
    if x%x_sum == 0:
        answer = True
    else:
        answer = False

    return answer