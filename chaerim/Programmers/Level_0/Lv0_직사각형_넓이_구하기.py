def solution(dots):
    answer = 0

    x_coords = [dot[0] for dot in dots]
    y_coords = [dot[1] for dot in dots]

    width = max(x_coords) - min(x_coords)
    height = max(y_coords) - min(y_coords)

    answer = width * height

    return answer