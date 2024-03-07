def solution(s):
    zero_count = 0
    binary = ""
    end_binary = False
    binary_count = 0

    while not end_binary:
        for i in s:
            if i == "0":
                zero_count += 1
            else:
                binary += "1"

        s = bin(len(binary))[2:]    # 이진법으로 나타내기(bin) : 6이면 0b110임 0b제거 - [2:]
        binary = ""
        binary_count += 1

        if len(s) == 1:
            end_binary = True

    answer = [binary_count, zero_count]

    return answer