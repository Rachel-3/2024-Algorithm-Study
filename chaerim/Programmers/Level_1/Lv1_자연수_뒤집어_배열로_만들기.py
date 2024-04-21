def solution(n):
    answer = []
    
    for num in str(n)[::-1]:
        answer.append(int(num))
    
    return answer