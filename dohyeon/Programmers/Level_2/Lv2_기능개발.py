import math
def solution(progresses, speeds):
    answer = []
    work = []
    for i in range(len(progresses)) :
        work.append(math.ceil((100 - progresses[i]) / speeds[i]))
    index = 0
    for i in range(len(work)) :
        if work[index] < work[i] :
            answer.append(i - index)
            index = i
    answer.append(len(work) - index)  
    return answer

print(solution([93, 30, 55],[1, 30, 5])) # 	[2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) #	[1, 3, 2]