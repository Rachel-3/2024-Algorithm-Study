def solution(my_string):
    my_str = []
    
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            my_str += my_string[i]
            
    my_str = list(map(int, my_str))
    my_str = sorted(my_str)
    answer = my_str
    
    return answer