n = int(input())
users = []
for i in range(n) :
    name, kor, eng, mat = input().split()
    users.append([name, int(kor), int(eng), int(mat)])

users.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in users :
    print(i[0])