koi = list(map(int, input().split()))

num_sum = 0
for i in koi:
    num_sum += i * i

print(num_sum % 10)