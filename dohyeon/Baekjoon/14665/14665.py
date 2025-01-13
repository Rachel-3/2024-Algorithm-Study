# 백준 14465 - 소가 길을 건너간 이유 5
# 분류 : 누적합

N, K, B = map(int, input().split())
check = [0] * N
for i in range(B) :
    check[int(input()) - 1] = 1

psum = [0] * N
psum[0] = check[0]
for i in range(1, N) :
    psum[i] = psum[i - 1] + check[i]

need = []
for i in range(0, N - K + 1) :
    # i ~ i + K - 1
    if i == 0 :
        num = psum[i + K - 1]
    else :
        num = psum[i + K - 1] - psum[i - 1]
    
    need.append(num)

print(min(need))