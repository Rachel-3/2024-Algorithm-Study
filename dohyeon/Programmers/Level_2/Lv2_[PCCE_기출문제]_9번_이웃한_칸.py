def isvalid(board, x, y) :
    x_max_length = len(board)
    y_max_length = len(board[0])
    if x < 0 or y < 0 or x >= x_max_length or y >= y_max_length :
        return False
    else :
        return True

def find_color(board, x, y) :
    return board[x][y]
    
def solution(board, h, w):
    answer = 0
    current_color = board[h][w]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4) :
        x = h + dx[i]
        y = w + dy[i]
        if (isvalid(board, x, y)) :
            if current_color == (find_color(board, x, y)) :
                answer += 1
    return answer