n = input()

left = n[:len(n)//2]
right = n[len(n)//2:]

left_sum = sum(map(int, list(left)))
right_sum = sum(map(int, list(right)))

if left_sum == right_sum :
    print("LUCKY")
else :
    print("READY")