def solution(a, d, included):
    answer = 0
    
    arithmetical_progression = []
    for i in range(1, len(included) + 1):
        arithmetical_progression.append(i)
        
    for i in range(len(included)):
        if i == 0:
            arithmetical_progression[i] = a
        else:
            arithmetical_progression[i] = arithmetical_progression[i-1] +d

    for i in range(len(included)):
        if included[i] == True:
            answer += arithmetical_progression[i]

    return answer