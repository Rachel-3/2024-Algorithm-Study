def solution(my_string, num1, num2):
    my_str = list(my_string)
    my_str[num1], my_str[num2] = my_str[num2], my_str[num1]
    answer = "".join(my_str)
    return answer