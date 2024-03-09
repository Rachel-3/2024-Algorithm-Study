def solution(my_string, m, c):
    answer = ''

    string = []
    for i in range(0, len(my_string), m):
        string.append(my_string[i:i+m])

    for i in range(0, len(string)):
        answer += string[i][c-1]

    return answer