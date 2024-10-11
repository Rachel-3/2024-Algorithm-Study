def solution(n, arr1, arr2):
    answer = []

    arr1 = [bin(arr)[2:].zfill(n) for arr in arr1]
    arr2 = [bin(arr)[2:].zfill(n) for arr in arr2]

    for i in range(n):
        string = ""
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                string += '#'
            else:
                string += ' '
        answer.append(string)

    return answer