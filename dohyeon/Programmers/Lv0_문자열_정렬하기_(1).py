def solution(my_string) :
    answer = []
    for i in my_string :
        if (i.isdigit() == True) :
            answer.append(i)
    answer = list(map(int, answer))
    answer.sort()
    return answer

print(solution("Ab12"))