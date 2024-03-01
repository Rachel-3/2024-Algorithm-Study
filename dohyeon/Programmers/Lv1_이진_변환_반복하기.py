def solution(s):
    answer = []
    remove_zero_count = 0
    loop_count = 1
    while True :
        remove_zero_count += s.count("0")
        s = s.replace("0", "")
        s = (bin(len(s)))
        s = str(s).replace("0b", "")
        if len(s) == 1 :
            break
        loop_count += 1
        
    answer = [loop_count, remove_zero_count]
    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))