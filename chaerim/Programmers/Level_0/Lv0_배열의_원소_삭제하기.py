def solution(arr, delete_list):
    answer = arr

    for num in delete_list:
        if num in answer:
            answer.remove(num)

    return answer