def find_divisors(n):
    count = 0

    for num in range(1, n + 1):
        if n%num == 0:
            count += 1

    return count

def solution(left, right):
    answer = 0

    for num in range(left, right + 1):
        divisors_count = find_divisors(num)

        if divisors_count % 2 == 0:
            answer += num
        else:
            answer -= num
    
    return answer