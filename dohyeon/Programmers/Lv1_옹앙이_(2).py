def solution(babbling):
    answer = 0
    noun = ["aya", "ye", "woo", "ma"]

    for i in babbling:
        compare_string = ""
        temp_string = "" 

        for j in i:
            compare_string += j
            if compare_string == temp_string:
                break
            if compare_string in noun:
                temp_string = compare_string
                compare_string = ""
        if compare_string == "":
            answer += 1

    return answer