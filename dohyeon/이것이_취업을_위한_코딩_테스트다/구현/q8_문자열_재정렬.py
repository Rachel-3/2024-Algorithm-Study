string = input()

string_pattern = ""
digit_pattern = ""
for i in string :
    if i.isdigit() :
        digit_pattern += i
    else :
        string_pattern += i

string_pattern = sorted(list(string_pattern))
digit_pattern = sum(map(int, list(digit_pattern)))

answer = "".join(string_pattern) + str(digit_pattern)
print(answer)