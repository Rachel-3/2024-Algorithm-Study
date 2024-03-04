def solution(X, Y):
    answer = []
   #  ''' 시간초과 메서드 1'''
    # for i in range(len(X)) :
        # ''' 시간초과 메서드 1'''
        # if X[i] in Y :
        #     numbers.append(X[i])
        #     Y = Y.replace(X[i], "", 1)
        # ''' 시간초과 메서드 2'''
        # try :
        #     index = (list(Y).index(X[i]))
        #     numbers.append(X[i])
        #     Y = Y.replace(X[i], "", 1)
        # except :
        #     pass
        # if X[i] in Y :
        #     numbers.append(X[i])
        #     Y = Y.replace(X[i], "", 1)
    for i in (set(X) & set(Y)) :
        for j in range(min(X.count(i), Y.count(i))) :
            answer.append(i)
    answer.sort(reverse = True)
    if len(answer) == 0 : return "-1"
    if answer[0] == "0" : return "0"
    answer = "".join(answer)
    return str(answer)

# print(solution("100", "2345")) #	"-1"
# print(solution("100", "203045")) #	"0"
# print(solution("100", "123450")) #	"10"
print(solution("12321", "42531")) #	"321"
# print(solution("5525", "1255")) # "552"
