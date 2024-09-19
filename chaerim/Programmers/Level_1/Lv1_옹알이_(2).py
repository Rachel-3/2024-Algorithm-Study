def solution(babbling):
    answer = 0
    talks = {"aya" : 1, "ye" : 2, "woo" : 3, "ma" : 4}

    for i in babbling:
        temp = i

        for talk, num in talks.items():
            temp = temp.replace(talk, str(num))

        if any(char.isalpha() for char in temp):
            continue

        stack = []
        use = True
        for char in temp:
            if char.isdigit():
                current_num = int(char)
                if stack and stack[-1] == current_num:
                    use = False
                    break
                stack.append(current_num)

        if use:
            answer += 1

    return answer