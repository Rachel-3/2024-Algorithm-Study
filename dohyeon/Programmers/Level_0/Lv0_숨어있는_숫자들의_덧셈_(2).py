import re
def solution(my_string):
    answer = 0
    numbers = map(int, re.findall(r'\d+', my_string))
    return sum(numbers)