def solution(board):
    answer = 0

    one_count = sum(sum(row) for row in board)

    if one_count == 1:
        return 1
    
    rows = len(board)
    cols = len(board[0])
    new_board = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        new_board[i][0] = board[i][0]
    
    for i in range(cols):
        new_board[0][i] = board[0][i]

    for i in range(1, rows):
        for j in range(1, cols):
            if board[i][j] == 1:
                new_board[i][j] = min(new_board[i-1][j], new_board[i][j-1], new_board[i-1][j-1]) + 1
                answer = max(answer, new_board[i][j])

    answer *= answer

    return answer