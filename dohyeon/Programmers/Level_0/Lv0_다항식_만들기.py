def solution(polynomial):
    answer = ''
    isPoly = 0
    isNomial = 0
    polynomial_list = (polynomial.split(" + "))
    for i in polynomial_list :
        if "x" in i :
            isPolyMental = i.replace("x", "")
            if len(isPolyMental) == 0 :
                isPoly += 1
            else :
                isPoly += int(isPolyMental)
        else :
            isNomial += int(i)

    
    if isPoly == 0 :
        answer = str(isNomial)
    elif isPoly > 1 and isNomial > 0:
        answer = str(isPoly) + "x + " + str(isNomial)
    elif isPoly > 1 and isNomial == 0 :
        answer = str(isPoly) + "x"
    elif isPoly == 1 and isNomial > 0 :
        answer = "x + " + str(isNomial)
    elif isPoly == 1 and isNomial == 0 :
        answer = "x"
    return answer

print(solution("3x + 7 + x"))
print(solution("3x"))
print(solution("3"))
print(solution("7x + 4 + 9 + 5x"))
print(solution("x + 1"))