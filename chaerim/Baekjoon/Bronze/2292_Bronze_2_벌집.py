n = int(input())

if n == 1:
    print(1)
else:
    layer = 1
    max_room = 1
    while max_room < n:
        max_room += 6 * layer
        layer += 1
    print(layer)