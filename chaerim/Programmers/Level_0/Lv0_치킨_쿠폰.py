def solution(chicken):
    answer = 0

    while chicken >= 10:
        quotient = chicken // 10
        remainder = chicken % 10

        answer += quotient
        chicken = quotient + remainder

    return answer