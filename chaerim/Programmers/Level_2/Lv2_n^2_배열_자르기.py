def solution(n, left, right):
    answer = []
    
    for index in range(left, right + 1):
        row = index // n
        col = index % n
        
        value = max(row, col) + 1
        answer.append(value)
    
    return answer