def solution(array):
    answer = []
    
    max_num = max(array)
    answer.append(max_num)
    answer.append(array.index(max_num))
    
    return answer