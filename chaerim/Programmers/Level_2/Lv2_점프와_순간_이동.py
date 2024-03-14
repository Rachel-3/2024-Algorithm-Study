def solution(n):
    ans = bin(n).count('1')

    return ans

'''
** 아래코드로 풀고 보니 생각나는 것을 위에 적용 **

def solution(n):
    ans = 0
    
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1

    return ans
'''


'''
** 시간 초과 **

def solution(n):
    ans = 1
    
    sum = 1
    teleport = 1
    while sum != n:
        if sum + teleport <= n:
            sum += teleport
            teleport *= 2
        else:
            ans += 1
            teleport = 1
            sum += 1

    return ans
'''