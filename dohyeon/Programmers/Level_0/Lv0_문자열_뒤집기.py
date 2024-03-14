def solution(my_string, s, e):
    answer = ''
    reverse_string = (my_string[s:e + 1])[::-1]
    answer += my_string[:s]
    answer += reverse_string
    answer += my_string[e + 1:]
    return answer

print(solution("Progra21Sremm3", 6, 12) == "ProgrammerS123")
print(solution("Stanley1yelnatS", 4, 10) == "Stanley1yelnatS")