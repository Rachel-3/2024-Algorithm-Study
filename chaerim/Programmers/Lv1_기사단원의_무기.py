def solution(number, limit, power):
    answer = 0
    strength = [0] * (number + 1)

    for num in range(1, number + 1):
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                if i*i == num:
                    strength[num] += 1
                else:
                    strength[num] += 2

    for i in strength:
        if i <= limit:
            answer += i
        else:
            answer += power

    return answer