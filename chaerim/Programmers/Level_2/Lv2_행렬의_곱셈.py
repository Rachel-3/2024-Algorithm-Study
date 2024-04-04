def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        arr_list = []
        for j in range(len(arr2[0])):
            number = 0
            for k in range(len(arr1[0])):
                number += arr1[i][k] * arr2[k][j]
            arr_list.append(number)
        answer.append(arr_list)

    return answer