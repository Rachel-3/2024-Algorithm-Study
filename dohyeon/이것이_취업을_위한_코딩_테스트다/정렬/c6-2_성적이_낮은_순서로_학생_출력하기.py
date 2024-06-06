n = int(input())

array = []

for i in range(n) :
    input_data = input().split(" ")
    name = input_data[0]
    score = input_data[1]
    array.append([name, score])

array = sorted(array, key = lambda n : n[1])

for i in array :
    print(i[0], end = ' ')