# 백준 110005 - 진법 변환 2
# 분류 : 수학

N, B = map(int, input().split())
s = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N :
    s += str(arr[N % B])
    N //= B

print(s[::-1])