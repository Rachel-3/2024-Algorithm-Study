import math

def solution(arr):
    answer = arr[:]

    arr_len = len(arr)
    square = int(math.pow(2, math.ceil(math.log(arr_len, 2))))

    answer += [0] * (square - arr_len)

    return answer

'''
math.log(x) : x의 자연로그 값 반환
math.log(x, base) : x의 로그 값 반환. 기본 로그의 밑은 자연로그(e). 밑(base)을 지정할 수 있음.
math.log2(x) : 	x의 2를 밑으로 가지는 로그 값 반환

math.ceil(x) : 인수와 같거나 큰 수 중에서 가장 작은 정수 반환
Math.pow(x,y) : x의 y제곱 반환
'''