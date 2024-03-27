def solution(A, B):
    answer = -1

    if A == B:
        answer = 0
    else:
        for i in range(1, len(A)):
            A = A[-1] + A[0:-1]
            if A == B:
                answer = i
                break

    return answer