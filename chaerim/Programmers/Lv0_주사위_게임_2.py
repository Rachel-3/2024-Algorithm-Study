def solution(a, b, c):
    answer = 0

    add = a + b + c
    square = a**2 + b**2 + c**2
    cube = a**3 + b**3 + c**3

    if a == b:
        if b == c:
            answer = add * square * cube
        else:
            answer = add * square
    elif a != b:
        if b == c:
            answer = add * square
        elif a == c:
            answer = add * square
        else:
            answer = add
    
    return answer