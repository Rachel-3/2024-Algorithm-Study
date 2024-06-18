n = int(input())
users = []
for i in range(n) :
    name, kor, eng, mat = input().split()
    users.append([name, int(kor), int(eng), int(mat)])

users.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in users :
    print(i[0])

'''
input )
12
Ju 50 60 100
Sa 80 60 50
Su 80 70 100
So 50 60 90
Ha 50 60 100
Ka 60 80 100
Do 80 60 100
Se 70 70 70
Wo 70 70 90 
Sanghyun 70 70 80
nsj 80 80 80
tae 50 60 90

Output )
Do
Sa
Su
nsj
Wo
Sanghyun
Se
Ka
Ha
Ju
So
tae
'''