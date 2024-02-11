def prime_number(num):
    if num < 2:
        return False
    for n in range(2, int(num**0.5) + 1):   # int(math.sqrt(num))
        if num % n == 0:
            return False
    return True

def solution(nums):
    answer = 0

    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                sum_number = nums[i] + nums[j] + nums[k]

                if prime_number(sum_number):
                    answer += 1

    return answer