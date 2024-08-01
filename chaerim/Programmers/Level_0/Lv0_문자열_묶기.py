def solution(strArr):
    answer = 0

    str_length_count = {}

    for char in strArr:
        char_len = len(char)
        if char_len in str_length_count:
            str_length_count[char_len] += 1
        else:
            str_length_count[char_len] = 1

    max_length = 0
    for length, count in str_length_count.items():
        if count > answer or (count == answer and length > max_length):
            answer = count
            max_length = length

    return answer