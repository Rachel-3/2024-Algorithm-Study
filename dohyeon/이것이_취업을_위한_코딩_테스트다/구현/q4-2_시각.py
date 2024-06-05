N = int(input())

answer = 0
M, S = 60, 60
for i in range(N + 1) :
    for minutes in range(M) :
        for second in range(S) :
            if "3" in str(second) + str(minutes) + str(i) :
                answer += 1
print(answer)