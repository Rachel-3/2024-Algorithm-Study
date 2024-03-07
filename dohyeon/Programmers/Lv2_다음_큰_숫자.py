def solution(n):
    current_one_count = str(bin(n)).count("1")
    i = 1
    while True :
        next_one_count = str(bin(n + i)).count("1")
        if current_one_count == next_one_count :
            return n + i
        else :
            i += 1

# Test
print(solution(78) == 83)
print(solution(15) == 23)