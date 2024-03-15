def solution(ineq, eq, n, m):
    if eq != "!" :
        query = str(n) + str(ineq + eq) + str(m)
    else :
        query = str(n) + str(ineq) + str(m) 
    answer = eval(query)
    if answer == True :
        return 1
    else :
        return 0