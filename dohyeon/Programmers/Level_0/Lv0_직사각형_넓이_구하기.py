def solution(dots):
    answer = 0
    x1, y1 = min(dots)
    x2, y2 = max(dots)
    answer = ((x2 - x1) * (y2 - y1))
    return answer