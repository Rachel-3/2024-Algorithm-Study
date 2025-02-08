# 1158 - 요세푸스 문제
N, K = map(int, input().split())
array = [i for i in range(1, N + 1)]
answer = []
index = 0 
for i in range(N) :
    index += K - 1
    if index >= len(array) :
        index = index % len(array)
    answer.append(str(array.pop(index)))
print("<",", ".join(answer), ">", sep = '')