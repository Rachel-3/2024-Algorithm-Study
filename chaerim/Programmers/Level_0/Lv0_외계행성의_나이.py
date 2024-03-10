def solution(age):
    answer = str(age)
    age_dic = {'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4', 'f':'5', 'g':'6', 'h':'7', 'i':'8', 'j':'9'}

    for key, value in age_dic.items():
        answer = answer.replace(value, key)
    
    return answer