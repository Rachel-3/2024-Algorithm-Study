def solution(arr):
    stk = []
    i = 0
    while True :
        if len(stk) == 0 :
            stk.append(arr[i])
            i += 1
        elif len(stk) > 0 and stk[-1] < arr[i] :
            stk.append(arr[i])
            i += 1
        elif len(stk) > 0 and stk[-1] >= arr[i] :
            stk.pop()
        
        if len(arr) == i :
            break
    return stk