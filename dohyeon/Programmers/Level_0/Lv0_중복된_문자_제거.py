def solution(my_string):
    answer = ''
    duplication_words = []
    for i in my_string :
        if i not in duplication_words :
            answer += i
            duplication_words.append(i)
    return answer