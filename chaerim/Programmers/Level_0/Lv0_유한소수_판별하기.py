def solution(a, b):
    answer = 1

    num_a = a
    num_b = b
    while num_b != 0:
        num_a, num_b = num_b, num_a%num_b

    gcd = num_a
    b = b//gcd
    while b != 1:
        if b%2 == 0:
            b //= 2
        elif b%5 == 0:
            b //= 5
        else:
            answer = 2
            break

    return answer