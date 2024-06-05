n, k = map(int, input().split(" "))

array_a = list(map(int, input().split(" ")))
array_b = list(map(int, input().split(" ")))

array_a.sort()
array_b.sort(reverse = True)

for i in range(k) :
    # array_a[i] = array_b[i] # 이렇게 하면, 만약 중복인 경우에는 어떻게 하지?
    if array_a[i] < array_b[i] :
        array_a[i], array_b[i] = array_b[i], array_a[i]
    else :
        break

print(sum(array_a))