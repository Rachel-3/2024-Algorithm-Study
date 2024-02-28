''' 시간 초과 코드 '''
'''
def prime_number_count(n) :
    divisorsList = []
    for i in range(1, n + 1):
        if (n % i == 0) :
            divisorsList.append(i)
    return len(divisorsList)
'''
''' 시간 복잡도 개선 '''
def prime_number_count(n) :
    result = 0
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            result += 1
            if i < n // i:
                result += 1
    return result

def solution(number, limit, power):
    answer = 0
    prime_number_list = []
    for i in range(1, number + 1) :
        prime_number_list.append(prime_number_count(i))
    for i in range(len(prime_number_list)) :
        if prime_number_list[i] > limit :
            prime_number_list[i] = power
    answer = sum(prime_number_list)
    return answer

print(solution(5, 3, 2))