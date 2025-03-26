vowels = set('aeiouAEIOU')

while True:
    line = input()
    if line == '#':
        break

    count = sum(1 for ch in line if ch in vowels)
    print(count)