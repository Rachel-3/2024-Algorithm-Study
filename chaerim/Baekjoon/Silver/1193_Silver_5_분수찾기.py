x = int(input())

line = 1
while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    numer = x
    deno = line - x + 1
else: 
    numer = line - x + 1
    deno = x

print(f"{numer}/{deno}")