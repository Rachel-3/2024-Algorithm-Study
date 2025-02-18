# 백준 1463 - 1로 만들기
# 분류 : DP

N = int(input())

# 사용할 수 있는 연산
# 1. 3으로 나누기 (3의 배수일 때만 사용 가능)
# 2. 2로 나누기 (2의 배수일 때만 사용 가능)
# 3. 1빼기 (언제나 사용가능)

a = [0] * (N + 1) # 길이가 N + 1, a[N]

a[1] = 0

for i in range(2, N + 1) :
    a[i] = 1 + a[i - 1]

    if i % 3 == 0 :
        a[i] = min(a[i], 1 + a[i // 3])
    if i % 2 == 0 :
        a[i] = min(a[i], 1 + a[1 // 2])

print(a[N])
