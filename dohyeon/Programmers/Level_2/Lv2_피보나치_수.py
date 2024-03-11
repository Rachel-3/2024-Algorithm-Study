''' 런타임 에러 & 시간초과 '''
'''
정확성: 42.9
합계: 42.9 / 100.0
'''
# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)
# def solution(n):
#     answer = fibo(n) % 1234567
#     return answer
''' 제귀 함수 -> 시간이 오래걸림 '''

def solution(n):
    answer = 0
    if n in {0, 1}:
        return n
    previous, answer = 0, 1
    for _ in range(2, n + 1):
        previous, answer = answer, previous + answer

    return answer % 1234567