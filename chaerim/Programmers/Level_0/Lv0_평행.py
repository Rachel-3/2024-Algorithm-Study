def finding_slope(s1, s2):

    x1, y1 = s1
    x2, y2 = s2

    return (y2 - y1) / (x2 - x1)

def solution(dots):
    answer = 0

    slopes = [
        finding_slope(dots[0], dots[1]), 
        finding_slope(dots[0], dots[2]), 
        finding_slope(dots[0], dots[3]), 
        finding_slope(dots[1], dots[2]), 
        finding_slope(dots[1], dots[3]), 
        finding_slope(dots[2], dots[3])]
    
    if slopes[0] == slopes[5] or slopes[1] == slopes[4] or slopes[2] == slopes[3]:
        answer = 1
    else:
        answer = 0

    return answer