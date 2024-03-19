def solution(myString, pat):
    answer = ''

    string = myString.replace(pat,'0')

    for i in range(len(string)-1, -1, -1):
        if string[i] == '0':
            answer = string[:i+1]
            break

    answer = answer.replace('0', pat)

    return answer