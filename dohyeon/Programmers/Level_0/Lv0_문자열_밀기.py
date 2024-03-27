def solution(A, B):
    answer = 0
    if A == B :
        return 0
    else :
        for i in range(1, len(A)) :
            A = A[-1] + A[0 : -1]
            if A == B :
                return i
    
    return -1