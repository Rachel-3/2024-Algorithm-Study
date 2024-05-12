from itertools import permutations
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_combinations(s):
    n = list(s)
    a = []
    for i in range(1, len(n)+1):
        a += list(permutations(n, i))
    b = []
    for i in a:
        b.append(int(''.join(i)))   
    b = list(set(b))
    return b

def solution(numbers):
    answer = 0
    lists = (generate_combinations(numbers))
    lists = list(map(int, lists))
    for i in lists :
        if is_prime(i) :
            answer += 1
    return answer