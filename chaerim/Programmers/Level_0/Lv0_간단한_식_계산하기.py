def solution(binomial):
    answer = 0

    num1, op, num2 = binomial.split()

    if op == '+':
        answer = int(num1) + int(num2)
    elif op == '-':
        answer = int(num1) - int(num2)
    elif op == '*':
        answer = int(num1) * int(num2)
    elif op == '/':
        answer = int(num1) / int(num2)

    return answer