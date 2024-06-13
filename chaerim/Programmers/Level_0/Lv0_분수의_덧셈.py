def solution(numer1, denom1, numer2, denom2):
    answer = []

    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2

    numer_num = numer   ## 유클리드 호제법 - 최대 공약수 계산하는 방법
    denom_num = denom   ## 나머지 0이 될 때 까지 반복
    while denom_num:    ## 최종적으로 나누는 수가 최대 공약수
        numer_num, denom_num = denom_num, numer_num % denom_num

    divisor = numer_num
    answer.append(numer // divisor)
    answer.append(denom // divisor)

    return answer
