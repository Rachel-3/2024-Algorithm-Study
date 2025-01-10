a = int(input())
count = 0
start = a

while True:
    count += 1
    tens = a // 10
    ones = a % 10
    
    new_ones = (tens + ones) % 10
    
    a = ones * 10 + new_ones
    
    if a == start:
        break

print(count)