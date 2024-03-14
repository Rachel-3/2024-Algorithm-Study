def isPrime(n) :
    count = 0
    for i in range(1, n + 1) :
        if n % i == 0 :
            count += 1
    if count >= 3 :
        return True
    return False

def solution(n):
    answer = 0
    for i in range(n + 1) :
        if isPrime(i) == True :
            answer += 1
    return answer