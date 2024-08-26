def solution(numbers):
    answer = ""

    number_dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    word = ""
    for char in numbers:
        word += char
        if word in number_dic:
            answer += str(number_dic[word])
            word = ""

    return int(answer)