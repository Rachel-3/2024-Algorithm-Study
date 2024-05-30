def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(len(B)) :
        if A[answer] < B[i] :
            answer += 1
    return answer