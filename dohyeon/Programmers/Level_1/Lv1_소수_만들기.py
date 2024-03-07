def is_prime_number(x) :
    for i in range(2, x) :
        if x % i == 0 :
            return False
    return True
    
def solution(nums) :
    answer = 0
    for i in range(len(nums)) :
        for j in range(i + 1, len(nums)) :
            for k in range(j + 1, len(nums)) :
                add_number_result = nums[i] + nums[j] + nums[k]
                if is_prime_number(add_number_result) == True :
                    answer += 1
    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))