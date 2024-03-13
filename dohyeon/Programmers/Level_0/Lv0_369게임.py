def solution(order):
    answer = 0
    for i in list(str(order)) :
        if int(i) % 3 == 0 and int(i) != 0 :
            answer += 1
    return answer

# i 가 0일때도 고려해야함.