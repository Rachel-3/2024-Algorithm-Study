def solution(quiz):
    answer = []
    for i in quiz :
        sik = i.split("=")[0]
        result = i.split("=")[1]
        
        if eval(sik) == int(result) :
            answer.append("O")
        else :
            answer.append("X")
        
        
    return answer