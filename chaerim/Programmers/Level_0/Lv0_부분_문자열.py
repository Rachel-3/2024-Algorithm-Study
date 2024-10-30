def solution(str1, str2):
    answer = 0

    if str1 in str2:
        answer = 1
    elif str1 not in str2:
        answer = 0

    return answer