def prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
    return factors

def solution(n):
    answer = (prime_factors(n))
    answer =  list(set(answer))
    answer.sort()
    return (answer)