# 백준 10988 - 팰린드롬인지 확인하기
# 분류 : 심화

word = input()

if len(word) % 2 == 1 :
    first = word[:len(word) // 2]
    end = word[len(word) // 2 + 1:]
    end = reversed(end)
    end = "".join(end)
    if first == end :
        print(1)
    else :
        print(0)
else :
    first = word[:len(word) // 2]
    end = word[len(word) // 2:]
    end = reversed(end)
    end = "".join(end)
    if first == end :
        print(1)
    else :
        print(0)