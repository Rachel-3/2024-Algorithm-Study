def solution(n, t, m, p):
    answer = ''
    chars = '0123456789ABCDEF'
    result = ''
    i = 0
    while len(result) < t * m:
        num_in_base_n = ''
        num = i
        if num == 0:
            num_in_base_n = '0'
        else:
            while num > 0:
                num_in_base_n = chars[num % n] + num_in_base_n
                num //= n
        result += num_in_base_n
        i += 1
    for j in range(t):
        answer += result[(j * m) + (p - 1)]
    
    return answer


print(solution(2, 4, 2, 1) == "0111")
print(solution(16, 16, 2, 1) == "02468ACE11111111")
print(solution(16, 16, 2, 2) == "13579BDF01234567")