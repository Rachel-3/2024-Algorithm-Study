def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)) :
        if i not in indices :
            answer += my_string[i]
    return answer

print(solution("apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3]) == "programmers")