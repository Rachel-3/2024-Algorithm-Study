def solution(n):
    answer = 0

    # n의 홀수의 약수 개수 구하기
    for i in range(1, n+1):
        if i%2 != 0 and n%i == 0:
            answer += 1

    return answer

'''통과 -> m개의 연속된 자연수의 합이 n이 되기 위해 조건 확인
def solution(n):
    answer = 0

    consecutive_num = 1
    while True:
        sum_num = (consecutive_num * (consecutive_num - 1)) // 2
        if sum_num >= n:
            break
        elif (n - sum_num) % consecutive_num == 0:
            answer += 1
        consecutive_num += 1

    return answer
'''