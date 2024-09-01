def solution(keyinput, board):
    answer = []

    x_max = (board[0] - 1) // 2
    y_max = (board[1] - 1) // 2

    start = [0, 0]
    for key in keyinput:
        if key == 'up':
            if start[1] < y_max:
                start[1] += 1
        elif key == 'down':
            if start[1] > -y_max:
                start[1] -= 1
        elif key == 'left':
            if start[0] > -x_max:
                start[0] -= 1
        elif key == 'right':
            if start[0] < x_max:
                start[0] += 1

    answer = start

    return answer