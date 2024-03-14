def solution(arr, flag):
    answer = []
    for i in range(len(flag)) :
        if flag[i] == True :
            for j in range(arr[i] * 2) :
                answer.append(arr[i])
        elif flag[i] == False :
            for j in range(arr[i]) :
                answer.pop()        
    return answer

print(solution([3, 2, 4, 1, 3], [True, False, True, False, False]) == [3, 3, 3, 3, 4, 4, 4, 4])