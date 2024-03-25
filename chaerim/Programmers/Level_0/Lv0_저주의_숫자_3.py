def solution(n):
    answer = 0

    count = 1
    while n > 0:
        if count%3 ==0 or '3' in str(count):
            count += 1
            continue

        answer = count
        n -= 1
        count += 1

    return answer