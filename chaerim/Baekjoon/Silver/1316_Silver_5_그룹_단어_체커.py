n = int(input())
c = 0

for _ in range(n):
    a = input()
    last = ""
    lst = []
    group_word = True

    for i in a:
        if i not in lst:
            lst.append(i)
            last = i
        else:
            if last == i:
                continue
            else:
                group_word = False
                break

    if group_word:
        c += 1

print(c)