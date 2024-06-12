def solution(myString, pat):
    answer = 0
    
    myString = myString.replace('A', "#")
    myString = myString.replace('B', 'A')
    myString = myString.replace('#', 'B')
    myString = myString.replace(pat, '0')
    
    if '0' in myString:
        answer = 1

    return answer