def solution(nums):
    answer = min(len(set(nums)), len(nums)/2)

    return answer