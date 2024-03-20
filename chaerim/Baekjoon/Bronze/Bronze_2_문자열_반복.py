list = []
for _ in range(10):
    num = int(input())
    emp = num%42
    if emp not in list:
        list.append(emp)    

print(len(list))