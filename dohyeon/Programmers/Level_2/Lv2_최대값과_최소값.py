def solution(s):
    answer = ''
    string_list = list(map(int, s.split(" ")))
    print(string_list)
    min_num = min(string_list)
    max_num = max(string_list)
    answer = str(min_num) + " " + str(max_num)
    return answer