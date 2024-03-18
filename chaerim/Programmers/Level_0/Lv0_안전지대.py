def solution(board):
    answer = 0

    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 1:
                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        if 0 <= i < len(board) and 0 <= j < len(board) and board[i][j] != 1:
                            board[i][j] = 'X'

    for x in board:
        for y in x:
            if y == 0:
                answer += 1

    return answer