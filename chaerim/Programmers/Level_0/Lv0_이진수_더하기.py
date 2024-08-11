def solution(bin1, bin2):
    answer = ''

    bin_sum = int(bin1, 2) + int(bin2, 2)
    answer += bin(bin_sum)[2:]

    return answer