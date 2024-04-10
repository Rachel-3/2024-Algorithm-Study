def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer


''' 시간 초과 '''
# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)) :
#         temp = numbers[i:]
#         number_max = max(temp)
#         check = 0
#         if number_max > numbers[i] :
#             for j in temp :
#                 if numbers[i] < j :
#                     answer.append(j)
#                     break
#         else :
#             answer.append(-1)
#     return answer
''' 시간초과 나서 단일 O(n)으로 바꾸기 위해서 스택 사용 '''