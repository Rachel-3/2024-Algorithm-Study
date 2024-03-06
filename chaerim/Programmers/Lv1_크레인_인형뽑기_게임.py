def solution(board, moves):
    answer = 0

    basket = []
    for move in moves:
        for _, y in enumerate(board):
            if y[move-1] != 0:
                basket.append(y[move-1])
                y[move-1] = 0
                break

    i = 0
    while i < len(basket)-1:
        if basket[i] == basket[i+1]:
            basket.pop(i)
            basket.pop(i)
            answer += 2
            i = 0
        else:
            i += 1
    
    return answer