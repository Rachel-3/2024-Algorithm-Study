# 백준 1343 - 폴리오미노
# 분류 : 그리디

board = input()

answer = ""
count = 0
check = False
for i in range(len(board)) :
    if board[i] == "X" :
        count += 1
        if count == 4 :
            answer += "AAAA"
            count = 0
    else :
        if count == 0 :
            answer += "."
        elif count == 1 :
            check = True
            break
        elif count == 2 :
            answer += "BB"
            count = 0
            answer += "."
        elif count == 3 :
            check = True
            break

if count == 1 :
    check = True
elif count == 2 :
    answer += "BB"
elif count == 3 :
    check = True

if not check :
    print(answer)
else :
    print(-1)