''' 시간초과 70 / 100'''
# from collections import deque

# def solution(queue1, queue2):
#     queue1 = deque(queue1)
#     queue2 = deque(queue2)
#     sum_q1 = sum(queue1)
#     sum_q2 = sum(queue2)

#     for i in range(300000) :
#         if sum_q1 == sum_q2 :
#             return i

#         if sum_q1 > sum_q2 :
#             num = queue1.popleft()
#             queue2.append(num)
#             sum_q1 -= num
#             sum_q2 += num

#         elif sum(queue1) < sum(queue2)  :
#             num = queue2.popleft()
#             queue1.append(num)
#             sum_q1 += num
#             sum_q2 -= num
#     return -1

from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    target = (sum_q1 + sum_q2) // 2
    
    if (sum_q1 + sum_q2) % 2 != 0:
        return -1
    
    max_operations = len(queue1) * 2 + len(queue2) * 2
    operations = 0

    while sum_q1 != target and operations < max_operations:
        if sum_q1 > target:
            num = queue1.popleft()
            sum_q1 -= num
            queue2.append(num)
            sum_q2 += num
        else:
            num = queue2.popleft()
            sum_q2 -= num
            queue1.append(num)
            sum_q1 += num
        operations += 1

    return operations if sum_q1 == target else -1



print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))

