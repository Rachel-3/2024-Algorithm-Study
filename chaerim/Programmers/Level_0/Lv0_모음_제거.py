def solution(my_string):
    answer = my_string

    vowel = {'a':'', 'e':'', 'i':'', 'o':'', 'u':''}

    for key, value in vowel.items():
        answer = answer.replace(key, value)

    return answer