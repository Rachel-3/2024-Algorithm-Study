# 백준 10798 - 세로읽기
# 분류 : 2차원 배열
results = []
for i in range(5) :
    string = input()
    results.append(string)

for j in range(15) :
    for i in range(5) :
        if j < len(results[i]) :
            print(results[i][j], end = "")