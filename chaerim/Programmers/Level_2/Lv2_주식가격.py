def solution(prices):
    price_len = len(prices)
    answer = [0] * price_len

    stack = []

    for i in range(price_len):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = price_len - j - 1

    return answer