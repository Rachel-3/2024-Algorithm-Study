def solution(my_string, is_prefix):
    answer = 0
    if (my_string.find(is_prefix)) == 0 :
        answer += 1
    return answer