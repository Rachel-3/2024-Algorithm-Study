n, b = map(int, input().split())

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

if n == 0:
    result = "0"
else:
    while n > 0:
        remainder = n % b
        result = digits[remainder] + result
        n //= b

print(result)