def solution(triangle):
    answer = 0
    current_floor = len(triangle) - 1
    
    while current_floor > 0 :
        for i in range(current_floor) :
            triangle[current_floor - 1][i] += max(triangle[current_floor][i], triangle[current_floor][i + 1])
        current_floor -= 1
    answer = triangle[0][0]
        
    return answer