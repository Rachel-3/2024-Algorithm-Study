def solution(arr, intervals):
    answer = []
    for start, end in intervals:
        answer.extend(arr[slice(start, end + 1)])
    return answer